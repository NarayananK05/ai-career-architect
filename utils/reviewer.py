from utils.gemini_app import gemini_chat
import os
import uuid
import tempfile
import docx2txt
import PyPDF2

def extract_resume_text(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if uploaded_file.name.lower().endswith(".pdf"):
        try:
            with open(tmp_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception as e:
            text = f"[PDF Error] Could not extract text: {e}"

    elif uploaded_file.name.lower().endswith(".docx"):
        try:
            text = docx2txt.process(tmp_path)
        except Exception as e:
            text = f"[DOCX Error] Could not extract text: {e}"

    else:
        text = "[Error] Unsupported file format."

    return text

def review_resume(uploaded_file, target_role, target_company):
    resume_text = extract_resume_text(uploaded_file)

    prompt = f"""
You are a professional AI resume reviewer.
Review the following resume and suggest improvements for the role of '{target_role}' at '{target_company}'.
Focus on tailoring the resume to match the skills, keywords, and impact required for the job.

Resume:
{resume_text}
"""
    feedback = gemini_chat(prompt)

    filename = f"reviewed_resume_{uuid.uuid4().hex}"
    os.makedirs("reviewed", exist_ok=True)
    html_path = os.path.join("reviewed", f"{filename}.html")

    html = f"""
    <html>
    <head><meta charset='utf-8'><title>Resume Review</title></head>
    <body style='font-family: Arial; padding: 30px;'>
    <h1 style='color: #1A5276;'>AI Resume Feedback</h1>
    <pre style='white-space: pre-wrap; font-size: 14px;'>{feedback}</pre>
    </body>
    </html>
    """
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    return feedback, None, html_path
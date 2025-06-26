# utils/reviewer.py
from utils.gemini_app import gemini_chat
import os
import uuid
import pdfkit

config = pdfkit.configuration(
    wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
)

def review_resume(file_bytes, target_role, target_company):
    # Extract text from uploaded resume
    resume_text = file_bytes.read().decode("utf-8") if isinstance(file_bytes, bytes) else file_bytes.read().decode("utf-8")

    # Create prompt
    prompt = f"""
You are a professional AI resume reviewer.
Review the following resume and suggest improvements for the role of '{target_role}' at '{target_company}'.
Focus on tailoring the resume to match the skills, keywords, and impact required for the job.

Resume:
{resume_text}
"""
    feedback = gemini_chat(prompt)

    # Save feedback as HTML and PDF
    filename = f"reviewed_resume_{uuid.uuid4().hex}"
    os.makedirs("reviewed", exist_ok=True)
    html_path = os.path.join("reviewed", f"{filename}.html")
    pdf_path = os.path.join("reviewed", f"{filename}.pdf")

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

    pdfkit.from_file(html_path, pdf_path, configuration=config)
    return feedback, pdf_path, html_path
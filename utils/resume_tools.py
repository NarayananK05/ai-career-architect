# utils/resume_tools.py
from utils.gemini_app import gemini_chat
from docx import Document
from docx.shared import Inches
import uuid
import os
import pdfkit

# PDFKit configuration
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
)

# Dummy layout list (simulate 300+ layouts)
def list_resume_layouts():
    return [f"Layout {i}" for i in range(1, 301)]

# Generate LaTeX resume
def generate_latex_resume(resume_text, layout_name):
    latex_template = f"""
\\documentclass[11pt]{{article}}
\\usepackage[a4paper,margin=1in]{{geometry}}
\\usepackage{{titlesec}}
\\usepackage{{color}}
\\usepackage{{graphicx}}
\\titleformat*\section{{\large\bfseries}}

\\begin{{document}}
\\begin{{center}}
    {{\\Huge\\bfseries Resume}} \\\\[1ex]
    {{\\large {layout_name}}}
\\end{{center}}
\\vspace{{1em}}

{resume_text.replace('\n', '\\\\')}

\\end{{document}}
"""

    filename = f"latex_resume_{uuid.uuid4().hex}"
    os.makedirs("generated", exist_ok=True)
    tex_path = os.path.join("generated", f"{filename}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_template)

    return latex_template, tex_path

# Generate DOCX and PDF resume

def generate_resume(user_input, uploaded_image=None):
    # Load prompt and get Gemini response
    prompt_template = open("prompts/resume_generator.txt", "r").read()
    filled_prompt = prompt_template.replace("{{user_input}}", user_input)
    resume_text = gemini_chat(filled_prompt, system="You are a professional resume writer.")

    # Create DOCX
    doc = Document()
    doc.add_heading('Resume', 0)

    if uploaded_image:
        doc.add_picture(uploaded_image, width=Inches(1.5))

    for line in resume_text.split("\n"):
        if line.strip() == "":
            continue
        if line.endswith(":"):
            doc.add_heading(line, level=1)
        else:
            doc.add_paragraph(line)

    # Save DOCX
    filename = f"generated_resume_{uuid.uuid4().hex}"
    docx_path = os.path.join("generated", f"{filename}.docx")
    os.makedirs("generated", exist_ok=True)
    doc.save(docx_path)

    # HTML content with styling
    html_content = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Resume</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                padding: 40px;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                text-align: center;
                color: #2E86C1;
            }}
            h2 {{
                color: #117A65;
                border-bottom: 1px solid #ccc;
                padding-bottom: 4px;
            }}
            p {{
                margin: 0.4em 0;
            }}
        </style>
    </head>
    <body>
        <h1>{user_input.splitlines()[0] if user_input else "Resume"}</h1>
        {''.join(f'<h2>{line}</h2>' if line.endswith(':') else f'<p>{line}</p>' for line in resume_text.splitlines() if line.strip())}
    </body>
    </html>
    """

    # Save HTML
    html_path = os.path.join("generated", f"{filename}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Convert to PDF
    pdf_path = os.path.join("generated", f"{filename}.pdf")
    pdfkit.from_file(html_path, pdf_path, configuration=config)

    return resume_text, docx_path, pdf_path, html_path

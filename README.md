# 🧠 AI Career Architect

**AI Career Architect** is a Streamlit web application that helps users create standout resumes, receive AI-powered reviews, and explore personalized learning plans and projects tailored to their dream roles.

---

## 🚀 Features

- ✍️ **Generate Resumes from Scratch**  
  Automatically build clean, structured resumes using Gemini AI, with optional profile photo.

- 📄 **Download Resume in DOCX Format**  
  PDF generation is **optional** (not supported on Streamlit Cloud). Download DOCX and convert locally.

- 🧠 **AI-Powered Resume Review**  
  Upload an existing resume and get feedback tailored to your **target role** and **company**.

- 💡 **Project & Learning Plan Generator**  
  Get role-based project ideas and curated learning roadmaps instantly.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Backend**: Google Gemini API (via `gemini_chat`)
- **Core Libraries**:
  - [`python-docx`](https://pypi.org/project/python-docx/) — Resume creation in DOCX
  - `uuid`, `os` — File handling
  - Optional: `pdfkit`, `weasyprint` (not used on Streamlit Cloud)

---

## 📁 Project Structure

```text
├── app.py                     # Main Streamlit app
├── prompts/
│   ├── resume_generator.txt   # Prompt for generating resumes
├── utils/
│   ├── gemini_app.py          # Gemini API wrapper
│   ├── resume_tools.py        # Resume generation logic (DOCX + HTML)
│   ├── reviewer.py            # AI resume reviewer
│   ├── project_tools.py       # Learning plan + project ideas
│   └── career_tools.py        # Career path suggestions
├── generated/                 # Generated resumes and HTML previews
└── .devcontainer/             # VS Code Dev Container support

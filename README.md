# AI Career Architect

**AI Career Architect** is a Streamlit web application designed to assist users in building professional resumes, receiving AI-powered resume reviews, and exploring tailored learning plans and project ideas based on their target job roles.

## Features

- Generate structured resumes with optional profile photo
- Download resumes in both DOCX and PDF formats
- Upload and review existing resumes using AI, tailored to specific job roles and companies
- Generate learning plans and project suggestions aligned with career goals

## Tech Stack

- Streamlit (frontend interface)
- Google Generative AI (Gemini API)
- Python libraries:
  - `python-docx` for DOCX creation
  - `pdfkit` with `wkhtmltopdf` for PDF generation

## Project Structure

├── app.py # Main application script
├── prompts/ # Prompt templates for resume and review
├── utils/
│ ├── resume_tools.py # Resume generation logic
│ ├── reviewer.py # AI resume reviewer
│ └── project_tools.py # Learning plan and project generator
└── generated/ # Output directory for resumes and reviews
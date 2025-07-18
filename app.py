import streamlit as st
import os
from utils.resume_tools import generate_resume
from utils.reviewer import review_resume
from utils.project_tools import generate_learning_plan, suggest_projects
from utils.career_tools import suggest_career_paths

if st.query_params.get("ping") == "1":
    st.write("alive")
    st.stop()

st.set_page_config(page_title="AI Career Architect", layout="centered")
st.title("🧠 AI Career Architect")
st.subheader("Your AI companion for careers 🚀")

tab1, tab2, tab3 = st.tabs(["🎓 Career Advisor", "📄 Resume Zone", "💡 Projects & Skills"])

# -----------------------------
# 🎓 Career Advisor Tab
# -----------------------------
with tab1:
    st.header("👨‍🏫 Career Guidance")

    stream = st.text_input("🧑‍🎓 Your Stream/Field (e.g., B.Tech CSE, B.Sc Bio)")
    interests = st.text_area("💭 Your Interests / Career Goals")

    if st.button("🎯 Suggest Career Paths"):
        if stream and interests:
            with st.spinner("Analyzing your background..."):
                suggestions = suggest_career_paths(stream, interests)
            st.success("🔍 Here are some career options for you!")
            st.markdown(suggestions)
        else:
            st.warning("Please fill out both your stream and interests.")

# -----------------------------
# 📄 Resume Zone Tab
# -----------------------------
with tab2:
    st.header("✍️ Generate Resume from Scratch")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn Profile (optional)")
    interests = st.text_area("Your Career Goals / Interests")

    resume_input = f"{name}\nEmail: {email}\nPhone: {phone}\nLinkedIn: {linkedin}\n\nCareer Goals:\n{interests}"

    uploaded_image = st.file_uploader("📸 Upload a Passport-Size Photo", type=["jpg", "jpeg", "png"])

    if st.button("🆕 Generate Resume from Scratch"):
        if not name or not email or not phone or not interests:
            st.error("Please fill in all required fields.")
        else:
            with st.spinner("Generating resume..."):
                generated_text, docx_path, pdf_path, html_path = generate_resume(resume_input, uploaded_image)

            st.success("✅ Resume generated successfully!")
            st.text_area("📝 Generated Resume", generated_text, height=300)

            st.markdown("### 🖼️ Resume Preview")
            with open(html_path, "r", encoding="utf-8") as html_file:
                st.components.v1.html(html_file.read(), height=700, scrolling=True)

            with open(docx_path, "rb") as docx_file:
                st.download_button(
                    "📄 Download as DOCX",
                    docx_file,
                    file_name=os.path.basename(docx_path),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        "📑 Download as PDF",
                        pdf_file,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )
            else:
                st.info("📄 PDF generation not supported on Streamlit Cloud. Please convert the DOCX to PDF locally.")

    # -------------------------
    # 🧠 Resume Reviewer Section
    # -------------------------
    st.divider()
    st.header("🧠 AI Resume Reviewer")

    uploaded_resume = st.file_uploader("📤 Upload Your Existing Resume (PDF or DOCX)", type=["pdf", "docx"], key="review_resume")
    target_role = st.text_input("🎯 Target Job Role", key="review_role")
    target_company = st.text_input("🏢 Target Company", key="review_company")

    if st.button("🧐 Review My Resume"):
        if uploaded_resume and target_role and target_company:
            with st.spinner("Analyzing your resume..."):
                suggestions, review_pdf_path, review_html_path = review_resume(uploaded_resume, target_role, target_company)

            st.success("✅ Review complete!")
            st.markdown("### 📌 Suggestions to Improve Your Resume")
            st.markdown(suggestions)

            if review_pdf_path and os.path.exists(review_pdf_path):
                with open(review_pdf_path, "rb") as pdf_file:
                    st.download_button("📥 Download Review as PDF", pdf_file, file_name=os.path.basename(review_pdf_path), mime="application/pdf")
            else:
                st.info("📄 PDF not available in this environment. View suggestions above or download the HTML version.")
                if review_html_path and os.path.exists(review_html_path):
                    with open(review_html_path, "r", encoding="utf-8") as f:
                        st.download_button("📥 Download Review as HTML", f, file_name=os.path.basename(review_html_path), mime="text/html")
        else:
            st.warning("Please upload a resume and enter both job role and company.")

# -----------------------------
# 💡 Projects & Skills Tab
# -----------------------------
with tab3:
    st.header("🔧 Projects & Skill Building")

    role = st.text_input("🎯 Target Role")

    if st.button("📘 Generate Learning Plan"):
        if role:
            with st.spinner("Creating learning plan..."):
                plan = generate_learning_plan(role)
            st.success("✅ Plan Ready!")
            st.markdown(plan)
        else:
            st.warning("Please enter a target role.")

    if st.button("🧪 Suggest Projects"):
        if role:
            with st.spinner("Generating project ideas..."):
                projects = suggest_projects(role)
            st.success("✅ Projects Suggested!")
            st.markdown(projects)
        else:
            st.warning("Please enter a target role.")

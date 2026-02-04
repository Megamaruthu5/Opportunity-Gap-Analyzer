import streamlit as st
from resume_parser import extract_skills_from_resume
from utils import get_skills_for_role
from gap_engine import analyze_skill_gap
from job_roles_data import job_roles

st.title("AI Opportunity Gap Analyzer")

# Resume input
resume_text = st.text_area("Paste your Resume Text")

# Job role dropdown
role = st.selectbox("Select Target Job Role", list(job_roles.keys()))

if st.button("Analyze"):
    user_skills = extract_skills_from_resume(resume_text)
    job_skills = get_skills_for_role(role)

    matched, missing, score = analyze_skill_gap(user_skills, job_skills)

    st.subheader("Match Score")
    st.write(f"{round(score,2)}%")

    st.subheader("Matched Skills")
    st.write(matched)

    st.subheader("Missing Skills")
    st.write(missing)

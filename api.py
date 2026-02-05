from fastapi import FastAPI, UploadFile, File, Form
from resume_parser import extract_text_from_pdf
from github_analyzer import analyze_github_profile
from gap_engine import analyze_skill_gap
from utils import extract_skills

app = FastAPI()

# Dummy job role skills dataset
JOB_SKILLS = {
    "data scientist": ["python", "machine learning", "statistics", "pandas", "numpy"],
    "web developer": ["html", "css", "javascript", "react", "nodejs"]
}

@app.post("/analyze")
async def analyze(
    job_role: str = Form(...),
    github_username: str = Form(...),
    resume: UploadFile = File(...)
):

    # Resume processing
    text = extract_text_from_pdf(resume.file)
    user_skills = extract_skills(text)

    job_skills = JOB_SKILLS.get(job_role.lower(), [])

    matched, missing, score = analyze_skill_gap(user_skills, job_skills)

    github_data = analyze_github_profile(github_username)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "score": score,
        "github": github_data
    }

from resume_parser import extract_skills_from_resume

resume_text = """
I have experience in Python, Machine Learning and Data Visualization.
I also worked with Pandas and GitHub.
"""

skills = extract_skills_from_resume(resume_text)

print("Extracted Skills:")
for skill in skills:
    print("-", skill)

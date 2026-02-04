from job_roles_data import job_roles

def get_skills_for_role(role):
    for job_role in job_roles:
        if job_role.lower() == role.lower():
            return job_roles[job_role]
    return []


SKILL_DATABASE = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Statistics",
    "Pandas",
    "NumPy",
    "SQL",
    "NLP",
    "Computer Vision",
    "TensorFlow",
    "PyTorch",
    "Git",
    "GitHub",
    "Data Visualization",
    "Matplotlib",
    "Seaborn"
]


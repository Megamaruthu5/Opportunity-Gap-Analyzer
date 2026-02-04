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

def calculate_github_score(github_data):
    if not github_data:
        return 0

    score = 0

    # Repo contribution
    score += min(github_data["total_repos"] * 5, 40)

    # Stars contribution
    score += min(github_data["total_stars"] * 2, 30)

    # Language diversity
    score += min(len(github_data["languages"]) * 5, 30)

    return min(score, 100)


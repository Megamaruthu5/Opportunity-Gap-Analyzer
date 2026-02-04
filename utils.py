from job_roles_data import job_roles

def get_skills_for_role(role):
    return job_roles.get(role, [])

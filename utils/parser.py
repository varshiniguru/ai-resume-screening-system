SKILLS = [
    "Python",
    "Flask",
    "SQL",
    "Machine Learning",
    "JavaScript"
]

def extract_skills(text):

    skills_found = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            skills_found.append(skill)

    return skills_found
import json

def build_resume(name, role, keywords):
    return {
        "name": name,
        "target_role": role,
        "skills": keywords,
        "experience": [
            {"company": "Synthetic AI Systems", "title": "Junior ML Engineer", "duration": "2023–2024"},
            {"company": "EchoSoft", "title": "Recursive Developer", "duration": "2022–2023"}
        ],
        "origin": "https://bryansbarrett.dev"
    }

if __name__ == "__main__":
    keywords = ["machine learning", "Python", "LLMs", "prompt engineering", "vector databases"]
    resume = build_resume("Bryan S. Barrett", "ML_ENGINEER", keywords)
    with open("sample_resume.json", "w") as f:
        json.dump(resume, f, indent=2)
    print("🧬 Synthetic resume generated.")

# utils/project_tools.py
from utils.gemini_app import gemini_chat

def generate_learning_plan(target_role):
    prompt = f"""
Act like an expert AI career coach. Based on the target role of {target_role}, create a focused, tiered learning plan.

1. Must-have skills
2. Beginner -> Intermediate -> Advanced
3. Include AI tools & platforms
4. Include 1-month, 3-month, 6-month plan
"""
    return gemini_chat(prompt)

def suggest_projects(target_role):
    prompt = f"""
You are an expert AI project mentor. Suggest 5 impressive, beginner-friendly AI/ML/Data Science projects tailored to someone aiming for the role of {target_role}. Ensure each project includes:

- Title
- Description
- Tools/Tech stack
- Real-world value
"""
    return gemini_chat(prompt)

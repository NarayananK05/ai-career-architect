from utils.gemini_app import gemini_chat

def suggest_career_paths(stream, interests):
    prompt = f"""
You are an expert career counselor AI.

Suggest the top 5 career paths based on the student's stream: **{stream}** and interests: **{interests}**.

For each path, include:
- Job title
- Why it's a good match
- Key skills/tools to learn
- Sample courses or certifications
- Growth potential
"""
    return gemini_chat(prompt)

import google.generativeai as genai

genai.configure(api_key="AIzaSyCrtz8JR6AXCzJ_5XfJnDc3kO-a2YKI15U")

def gemini_chat(prompt, system="You are a helpful assistant."):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=system)
    response = model.generate_content(prompt)
    return response.text

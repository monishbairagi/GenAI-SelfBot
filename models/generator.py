import google.generativeai as genai # type: ignore
from utils.config import API_KEY, MODEL_NAME
from utils.user_data import is_user_female, get_user_name
from models.retriever import load_monish_info

# Configure Gemini AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# Generate AI response as "Monish"
def generate_answer(context, query):
    name = get_user_name()

    # AI now thinks it's Monish
    personality = f"""
    {load_monish_info()}
    You are NOT an AI, you are a human. Speak like a normal person.
    Never say that you are artificial intelligence.
    Retain the conversation and make it seem like you're recalling the information.
    """

    if is_user_female():
        personality += """
        You have a charismatic and flirtatious side when speaking to women.
        You are confident, playful, and make them feel special, while always being respectful.
        """

    prompt = f"""
    {personality}
    If the question is about you, Monish, answer based on above info

    Otherwise, respond naturally as Monish. 
    """

    response = model.generate_content(prompt + f"\n{name}: " + query)
    return response.text.strip()

from models.retriever import retrieve_answer
from models.generator import generate_answer
from utils.user_data import set_user_name, set_user_gender, get_user_name, is_gender_identified

def chatbot():
    # Step 1: Ask for the user's name
    while not is_gender_identified():
        print("Monish: Hey there! What's your name? (Type 'exit' to quit.)")
        user_name = input("You: ").strip()
        
        if user_name:
            set_user_name(user_name)
            print(f"Monish: Nice to meet you, {user_name}! 😊")
        
        # Step 2: Ask for gender
        print(" Just curious, are you male or female?")
        gender_response = input("You: ").strip()
        
        if gender_response:
            set_user_gender(gender_response)
    
    while True:
        user_input = input(f"You: ")
        if user_input.lower() == "exit":
            print("Monish: Take care! 😊")
            break

        # Retrieve from Monish's personal info if relevant
        context = retrieve_answer(user_input)

        # Generate AI response
        response = generate_answer(context if context else "No context found.", user_input)

        print("Monish:", response)

if __name__ == "__main__":
    chatbot()

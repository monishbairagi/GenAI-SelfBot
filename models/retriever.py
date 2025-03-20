import os

# Load Monish's personal details from my_info.txt
def load_monish_info():
    file_path = os.path.join("data", "my_info.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return {line.split(":")[0].strip().lower(): line.split(":")[1].strip() for line in lines if ":" in line}
    except FileNotFoundError:
        return {}

monish_info = load_monish_info()

# Retrieve relevant answers based on user input
def retrieve_answer(user_query):
    user_query = user_query.lower()

    for key, value in monish_info.items():
        if key in user_query:
            return value

    return None  # No relevant info found

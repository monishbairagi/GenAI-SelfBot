import os
from flask import Flask, render_template, request, session
from models.retriever import retrieve_answer
from models.generator import generate_answer
from utils.user_data import set_user_name, set_user_gender
from flask_session import Session  # To store user data across requests

app = Flask(__name__)

# Configure session to use filesystem (store user data)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    session.clear()  # Reset session on fresh start
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form["msg"].strip()

    # Step 1: Ask for Name
    if "user_name" not in session:
        session["user_name"] = user_message
        set_user_name(user_message)
        return f"Nice to meet you, {user_message}! 😊 Just curious, are you male or female?"

    # Step 2: Ask for Gender
    if "user_gender" not in session:
        session["user_gender"] = user_message
        set_user_gender(user_message)
        return f"Thanks! You can now start chatting with me. Ask me anything! 😊"

    # Step 3: Normal Conversation
    context = retrieve_answer(user_message)
    bot_reply = generate_answer(context if context else "No context found.", user_message)
    return bot_reply

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
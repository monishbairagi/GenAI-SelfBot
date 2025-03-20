import os

# API Key for Gemini AI
API_KEY = "AIzaSyCr-syj1BShfK2sT7si7i_Zka8YrYWWbAQ"

# Gemini Model to Use
MODEL_NAME = "gemini-1.5-flash"  # You specified this model

# Path to your personal info file
INFO_FILE = os.path.join(os.getcwd(), "data", "my_info.txt")

# Path to store vectorized embeddings
VECTOR_STORE = os.path.join(os.getcwd(), "data", "my_info_embeded_vectors.pkl")

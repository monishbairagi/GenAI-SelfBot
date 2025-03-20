# Store user details
user_info = {"name": None, "gender": None}

# Function to set user name
def set_user_name(name):
    user_info["name"] = name

# Function to set user gender
def set_user_gender(gender):
    if gender.lower() in ["male", "man", "boy", "m"]:
        user_info["gender"] = "male"
    elif gender.lower() in ["female", "woman", "girl", "f"]:
        user_info["gender"] = "female"
    else:
        user_info["gender"] = "unknown"

# Function to check if gender is identified
def is_gender_identified():
    return user_info["gender"] is not None

# Function to get user name
def get_user_name():
    return user_info["name"] or "User"

# Function to check if user is female
def is_user_female():
    return user_info["gender"] == "female"

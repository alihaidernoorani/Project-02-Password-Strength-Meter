import re
import streamlit as st
import string, random

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.text("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.text("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.text("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.text("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

    return score

def password_generator(numbers, uppercase, symbols, password_length):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*"
    generatedpassword = ''.join(random.choice(characters) for _ in range(password_length))
    return generatedpassword

# Get user input

st.title("🔒 Password Checker & Generator")
password = st.text_input("Enter your password: ")
if st.button("Check Password"): 
    score = check_password_strength(password)

# Password Generator
st.subheader("Generate a Secure Password")
col1, col2 = st.columns(2)
with col1:
    password_length = st.slider(label="Password length", min_value=8, max_value=32, step=1, value=12)
    uppercase = st.checkbox("Include Uppercase Letters", value=True)
    numbers = st.checkbox("Include Numbers", value=True)
    symbols = st.checkbox("Include Symbols",  value=True)
    button = st.button("Generate Password")
with col2:
    if button:
        generated_password = password_generator(uppercase, numbers, symbols, password_length)
        st.success(f"🔑 Your Generated Password: `{generated_password}`")
import re 
import streamlit as st
import string, random

def check_password_strength(password):
    score = 0

    st.markdown("### 🧪 Password Strength Feedback")
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.warning("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.warning("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.warning("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

    return score

def password_generator(password_length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(password_length))

# Title
st.title("🔒 Password Strength Checker & Generator")

# Check Password
st.header("🔍 Check Your Password Strength")
password = st.text_input("Enter your password:", type="password")
if st.button("Check Password"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password before checking.")

# Divider
st.markdown("---")

# Password Generator
st.header("⚙️ Generate a Secure Password")
password_length = st.slider("Choose password length:", min_value=8, max_value=32, value=12)

if st.button("Generate Password"):
    generated_password = password_generator(password_length)
    st.success("🔑 Your secure password is ready:")
    st.code(generated_password, language="")


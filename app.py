import streamlit as st
import random

from Health_Chat_bot import (
    extract_symptoms,
    predict_disease,
    cols,
    getDescription,
    getprecautionDict,
    description_list,
    precautionDictionary,
    quotes,
)

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="AI Healthcare Chatbot",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------

getDescription()
getprecautionDict()

# -----------------------------
# SIDEBAR (ONLY SIDEBAR HERE)
# -----------------------------

with st.sidebar:
    st.image("assets/doctor.jpg", width=160)
    st.title("🩺 AI Healthcare")

    st.markdown("---")

    st.success("Disease Prediction")
    st.success("AI Powered")
    st.success("Health Tips")
    st.success("Precautions")
    st.success("Confidence Score")

    st.markdown("---")

    st.info("AI-based symptom checker for educational use only.")

    st.caption("Made with ❤️ using Streamlit")

# -----------------------------
# MAIN HEADER
# -----------------------------

col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/doctor.jpg", width=180)

with col2:
    st.markdown(
        "<div class='main-title'>🩺 AI Healthcare Chatbot</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Your Health, Our Priority ❤️</div>",
        unsafe_allow_html=True
    )

    st.info("""
This AI system predicts possible diseases based on symptoms
using Machine Learning.

⚠ Educational purpose only — not medical advice.
""")

# -----------------------------
# PATIENT INFO
# -----------------------------

st.markdown("---")
st.subheader("👤 Patient Information")

c1, c2 = st.columns(2)

with c1:
    name = st.text_input("Full Name")
    age = st.number_input("Age", 1, 120)

with c2:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# -----------------------------
# SYMPTOMS
# -----------------------------

st.markdown("---")
st.subheader("💬 Describe Your Symptoms")

symptoms = st.text_area(
    "",
    height=150,
    placeholder="Example: fever, cough, headache..."
)

predict = st.button("🔍 Predict Disease", use_container_width=True)

if predict:
    if symptoms.strip() == "":
        st.warning("⚠ Please enter symptoms first")
    else:
        # extract symptoms (FIXED)
        user_symptoms = extract_symptoms(symptoms, cols)

        # predict disease
        prediction = predict_disease(user_symptoms)

        st.markdown("---")
        st.success("🧠 Prediction Result")

        st.markdown(f"""
        <div class='card'>
            <h3>🦠 Disease: {prediction[0]}</h3>
            <p>📊 Confidence: {prediction[1]}%</p>
        </div>
        """, unsafe_allow_html=True)

        desc = description_list or {}
        st.info(desc.get(prediction[0], "No description available"))
        
        precautions = precautionDictionary.get(prediction[0], [])

st.markdown(f"""
<div style="
    background-color: #d9f2ff;
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #0b74a5;
">
    <h4 style="color:#0b74a5;">💊 Precautions</h4>
    <ul style="color:#ffd700; font-weight:600;">
        {''.join([f"<li>{p}</li>" for p in precautions])}
    </ul>
</div>
""", unsafe_allow_html=True)
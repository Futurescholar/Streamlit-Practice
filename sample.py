import streamlit as st

st.set_page_config(page_title="Advanced BMI Calculator", page_icon="⚖️", layout="centered")
st.title("⚖️ Advanced BMI Calculator")

# Sidebar inputs
st.sidebar.header("Enter your details")

weight = st.sidebar.number_input("Weight (kg)", min_value=1, max_value=500, step=1, format="%d")
height = st.sidebar.number_input("Height (cm)", min_value=50.0, max_value=300.0, step=0.1, format="%.1f")

# Calculate BMI when button clicked
if st.sidebar.button("Calculate BMI"):
    if weight <= 0 or height <= 0:
        st.error("Please enter valid positive numbers for weight and height.")
    else:
        bmi = weight / ((height / 100) ** 2)
        bmi_rounded = round(bmi, 2)
        
        # Determine BMI category and message
        if bmi <= 18.5:
            category = "Underweight"
            color = "orange"
            advice = "You are underweight."
        elif bmi <= 24.9:
            category = "Healthy weight"
            color = "green"
            advice = "Keep it up! You have a healthy weight."
        elif bmi <= 29.9:
            category = "Overweight"
            color = "yellow"
            advice = "Work on your diet and try to exercise."
        else:
            category = "Obese"
            color = "red"
            advice = "You are obese. Please consult a healthcare professional."
        
        # Show results
        st.markdown(f"### Your BMI is: **{bmi_rounded}**")
        st.markdown(f"<span style='color:{color};font-weight:bold;font-size:22px'>{category}</span>", unsafe_allow_html=True)
        st.info(advice)

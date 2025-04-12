import streamlit as st

# Page settings
st.set_page_config(page_title="BMI Calculator", page_icon="🧮")

# Title
st.title("🧮 Body Mass Index (BMI) Calculator")

st.markdown("---")

# Input section
st.subheader("📋 Enter Your Details")
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

with col2:
    height = st.number_input("Height (meters)", min_value=0.0, step=0.01)

# BMI Calculation
if st.button("💡 Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.success(f"📏 Your BMI is: **{bmi:.2f}**")

        # BMI category
        if bmi < 18.5:
            st.warning("⚠️ You are **underweight**.")
        elif 18.5 <= bmi < 24.9:
            st.info("✅ You have a **normal weight**. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **overweight**.")
        else:
            st.error("🚨 You are **obese**. Consider consulting a doctor.")
    else:
        st.error("❌ Please enter valid weight and height.")

# Display BMI Categories Chart
st.markdown("---")
st.subheader("📊 BMI Categories")
st.markdown("""
| BMI Range | Category       |
|-----------|----------------|
| Less than 18.5 | Underweight   |
| 18.5 – 24.9   | Normal weight |
| 25.0 – 29.9   | Overweight    |
| 30.0 and above | Obese         |
""")

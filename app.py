import streamlit as st
import joblib
import pandas as pd

# Load the saved model
@st.cache_resource
def load_model():
    return joblib.load('resilience_sync_rf.pkl')

model = load_model()

# Title
st.title("Resilience Sync: AI Burnout Risk Predictor")

# Subheader
st.subheader("Enter your details to assess your burnout risk:")

st.write("""This tool leverages a machine learning model to identify psychological and 
cognitive 'taxes' of AI integration. By understanding these factors, you can take proactive steps to manage your well-being""")

# Use columns to make it look cleaner
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    experience = st.number_input("Years of Experience", 0, 50, 5)
    ai_hours = st.number_input("AI Usage (Hours/Day)", 0, 24, 2)

with col2:
    anxiety = st.slider("AI Anxiety Score", 1, 10, 5)
    sleep = st.number_input("Sleep (Hours/Night)", 0, 24, 7)
    cognitive_load = st.slider("Cognitive Load Score", 1, 10, 5)


if st.button("Predict Burnout Risk", type="primary"):
    input_df = pd.DataFrame({
        'Age': [age],
        'Years_Experience': [experience],
        'AI_Hours_Per_Day': [ai_hours],
        'Skill_Anxiety_Score': [anxiety],
        'Sleep_Hours_Per_Night': [sleep],
        'Cognitive_Load_Score': [cognitive_load] 
    })
    
    risk = model.predict(input_df)[0]
    
    st.divider()
    
    # Results
    if risk == 0:
        st.success("### ✅ Low Burnout Risk")
        st.write("You are showing strong resilience markers.")
    elif risk == 1:
        st.warning("### ⚠️ Moderate Burnout Risk")
        st.write("Consider monitoring your cognitive load and prioritizing sleep.")
    else:
        st.error("### 🚨 High Burnout Risk")
        st.write("High risk detected. It may be time to address AI anxiety or workflow overload.")  



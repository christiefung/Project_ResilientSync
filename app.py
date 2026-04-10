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

    st.subheader("Strategic Management Plan")
    
    # Instead of showing results in employees' perspectives, provide recommendations and actions based on the risk level:
    if risk == 0:
        st.success("### ✅ Low Burnout Risk")
        st.write("**Action:** This employee is a 'Reilience Syncer' - they are adapting well to AI integration." \
        "Encourage them to maintain their current habits and consider pairing them with more anxious junior staff and sharing their strategies with them.")
    elif risk == 1:
        st.warning("### ⚠️ Moderate Burnout Risk")
        if anxiety >= 7:
            st.write("**Action:** Authorize a Low-Risk Strategic Pilot. Task the employee with solving a real workflow bottleneck using AI.")
            
            with st.expander("The Strategic Intervention"):
                st.markdown("""
                            **Objective:** Restore professional security by proving human indispensability.
                            * **Hybrid Project Assignment:** Task the employee with project where AI handles the 'grunt work' (e.g., drafting/data cleanup) whereas the employee provides the strategic pivot.'
                            * **The 'AI Supervisor' Role:** By letting them *optimize* the tool for their own job, they prove to themselves that the tool is a utility they control, not a replacement that controls them.
                            * **Output:** The end result is a new guide that the employee can present to the team, boosting their status as an AI-subject matter expert and restoring their sense of professional value.
                            """)
        
        else:
            st.write("**Action:** Focus on biological resilience - encourage better sleep, regular breaks, and physical activity to help manage cognitive load. " \
            "Evaluate if evening AI-usage is bleeding into sleep time and encourage setting boundaries around work hours.")
    else:
        st.error("### 🚨 High Burnout Risk")
        if experience < 5:
            st.write("**Action:** Identity Anchoring: This employee feels their core value is threatened. Managers should explicitly decouple their " \
            "professional worth from task-automation and focus on their 'human-in-the-loop' creative oversight. ")
        else:
            st.write("**Action:** Cognitive Offloading: This senior professional is likely over-extending. Audit their 'Interruptions Per Day' and enforce deep-work blocks.")  



 


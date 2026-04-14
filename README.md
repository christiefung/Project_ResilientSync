# Project_ResilientSync
** Identifying hidden burnout risks in teams adopting AI through Machine Learning

Project Overview: Project_ResilientSync is a decision-support tool designed to uncover the psychological and cognitive "taxes" of AI integration. Unlike traditional surveys that focus on usage hours, this model leverages predictive analytics to identify vulnerability gaps and provide targeted management strategies.

## Live Interactive Dashboard
**Explore the Model: ** https://resilient-sync.streamlit.app/
*Input team metrics (e.g., Anxiety, Cognitive Load, Career Phase) to receive real-time risk assessments and management strategies.*

## Key Insights & Strategy
After performing  exploratory data analyses (EDA) and optimizing a Random Forest Classifier (Acc = 0.81), the  following insights were identified:


1. The "Usage Myth" and The Cognitive Tax:
AI exposure time (r= -0.02) is not a main driver of burnout. Instead, cognitive load is the number 1 predictor (importance: 0.21)

The strategy (Cognitive offloading): Organizations must audit AI workflows to ensure tools are reducing, rather than compounding, the mental load of staff

2. The Junior Vulnerability:
While overall AI-replacement anxiety is a moderate predictor of burnout risk, its impact is non-linear. Statistical modeling (OLS Regression) confirms that career stage is a critical moderator of AI-related stress.  Early-career employees exhibit a 52% steeper burnout-response slope (p< .0001) compared to Mid-Level/Seniors and Experts when facing identical levels of AI-replacement anxiety. 

The strategy (Identity Anchoring): Implement mentorship programs for Juniors to decouple their professional value from tasks now automated by AI, focusing insetad on high-level strategy and 'human-in-the-loop' decision making.


3. Anxiety Invariance: Existential vs. Functional Fear: 
The moderation analysis reveals that AI-replacement anxiety remains a constant driver of burnout regardless of perceived tool usefulness. 

The strategy (Psychological Safety): Companies and organizations should move beyond "passive training" (e.g., webinars/videos) and 'usage mandates" (e.g., monitoring number of hours or tokens spent on the AI tools). Instead, leadership should task anxious staff, particularly the vulnerable Junior staff, with architecting AI-driven solutions such that they move from a 'subject of automation' to an 'architect of optimization'. This restores self-efficacy and creates psychological safety that halts the burnout-response slope identified in the model.

4. Biological Buffers: 
Sleep hours outperformed AI-specific variables in predicting resilience, suggesting burnout is a holistic issue, not just a technical one. Additionally, hands-on time using AI correlates with lower anxiety (r = -0.21)

The strategy (Demystification): High frequency use of AI tools can demystify technology and lower the baseline of replacement fear

## The Product: ResilientSync Dashboard
To translate these insights into action, I developed a **Streamlit-based Decision Support Tool** for HRBP and Team Leads.

* **Real-time Risk Scoring:** Utilizes the Random Forest backend to categorize employee risk (Low/Moderate/High).
* **Dynamic Strategy Engine:** Generates tailored interventions based on user profile. 
    * *Example:* If the user is a Junior with high anxiety, the tool triggers an **Identity Anchoring** protocol.
* **Feature-Correct Inference:** Built with a robust preprocessing pipeline that handles scalar-to-dataframe conversion for model stability.

### Tech Stack
* **Analysis:** Python (Pandas, NumPy, Scipy)
* **Modeling:** Scikit-Learn (Random Forest, OLS Regression)
* **Productization:** Streamlit (UI), Joblib (Model Serialization)

## Methodology:
1. EDA: Correlation heatmapping, multivariate distribution analysis to investigate the behavior of multiple variables (anxiety, cognitive load, sleep etc) on burnout risk

2. Moderation testing using perceived AI usefulness and career-phase binning to identify non-linear burnout triggers

3. OLS regression: conducted an interaction-effect model (Burnout ~ Anxiety x Career_phase) to quantify the unique vulnerability of the Junior group

4. Predictive Modeling: optimized a Random Forest Classifier (Acc = 0.81) to automate risk detection across the organization

## Future Directions:
Sample Imbalance: The "High Risk" category represented a tiny fraction of the dataset (< 1%). While the model's sensitivity improved after feature selection, further data collection or synthetic oversampling (SMOTE) would be required for a production-level safety tool.

Self-Report Bias: Data is based on self-reported surveys; objective metrics (e.g., actual screen time or biometric stress data) would strengthen the predictive power.

Cross-Sectional vs. Longitudinal: This is a snapshot in time. A longitudinal study would better track how burnout evolves as an employee's AI proficiency grows.







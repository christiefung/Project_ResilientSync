# Project_ResilientSync
Project Overview: This tool identifies hidden burnout risks in teams adopting AI. Unlike traditional surveys that focus on usage hours, this model leverages machine learning to uncover the psychological and cognitive "taxes" of AI integration.

Key Insights & Strategy
After performing  exploratory data analyses (EDA) and optimizing a Random Forest Classifier (Acc = 0.81), the  following insights were identified:


1. The "Usage Myth" and The Cognitive Tax:
AI exposure time (r= -0.02) is not a main driver of burnout. Instead, cognitive load is the number 1 predictor (importance: 0.21)

The strategy (Cognitive offloading): Organizations must audit AI workflows to ensure tools are reducing, rather than compounding, the mental load of staff

2. The Junior Vulnerability:
While overall AI-replacement anxiety is a moderate predictor of burnout risk, its impact is non-linear. Statistical modeling (OLS Regression) confirms that career stage is a critical moderator of AI-related stress.  Early-career employees exhibit a 52% steeper burnout-response slope (p< .0001) compared to Mid-Level/Seniors and Experts when facing identical levels of AI-replacement anxiety. 

The strategy (Identity Anchoring): Implement mentorship programs for Juniors to decouple their professional value from tasks now automated by AI, focusing insetad on high-level strategy and 'human-in-the-loop' decision making.


3. Anxiety Invariance: Existential vs. Functional Fear: 
The moderation analysis reveals that AI-replacement anxiety remains a constant driver of burnout regardless of perceived tool usefulness. 

The strategy (Psychological Safety): Optimizing for "productivity" or "tool usefulness" will not naturally solve the burnout problem. Leadership must address the psychological safety of the workplace as a separate initiative from technical AI training.

4. Biological Buffers: 
Sleep hours outperformed AI-specific variables in predicting resilience, suggesting burnout is a holistic issue, not just a technical one. Additionally, hands-on time using AI correlates with lower anxiety (r = -0.21)

The strategy (Demystification): High frequency use of AI tools can demystify technology and lower the baseline of replacement fear

Methodology:
1. EDA: Correlation heatmapping, multivariate distribution analysis to investigate the behavior of multiple variables (anxiety, cognitive load, sleep etc) on burnout risk

2. Moderation testing using perceived AI usefulness and career-phase binning to identify non-linear burnout triggers

3. OLS regression: conducted an interaction-effect model (Burnout ~ Anxiety x Career_phase) to quantify the unique vulnerability of the Junior group

4. Predictive Modeling: trained a Random Forest Classifier (Acc = 0.81) to automate risk detection across the organization


Future Directions:
Sample Imbalance: The "High Risk" category represented a tiny fraction of the dataset (< 1%). While the model's sensitivity improved after feature selection, further data collection or synthetic oversampling (SMOTE) would be required for a production-level safety tool.

Self-Report Bias: Data is based on self-reported surveys; objective metrics (e.g., actual screen time or biometric stress data) would strengthen the predictive power.

Cross-Sectional vs. Longitudinal: This is a snapshot in time. A longitudinal study would better track how burnout evolves as an employee's AI proficiency grows.






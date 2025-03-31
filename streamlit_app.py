import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("stacking_model.pkl")

# Define the features used for training
features = ['encounter_id', 'patient_nbr', 'race', 'gender', 'age', 'weight', 
            'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 
            'time_in_hospital', 'payer_code', 'medical_specialty', 'num_lab_procedures', 
            'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 
            'number_inpatient', 'diag_1', 'diag_2', 'diag_3', 'number_diagnoses', 
            'max_glu_serum', 'A1Cresult', 'metformin', 'repaglinide', 'nateglinide', 
            'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 
            'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 
            'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin', 
            'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone', 
            'metformin-rosiglitazone', 'metformin-pioglitazone', 'change', 'diabetesMed', 
            'admission_type_description', 'weight_flag', 'outlier_flag']

# Define categorical features that need encoding
categorical_features = ['race', 'gender', 'admission_type_id', 'admission_source_id']

# Streamlit app title
st.title("Diabetes Readmission Prediction")

# Input Form for Features
st.header("Enter Patient Details")

# Generate inputs dynamically for all features
user_inputs = {}
for feature in features:
    if feature in categorical_features:
        user_inputs[feature] = st.text_input(f"{feature} (e.g., 'Caucasian', 'Male'):")
    elif feature in ['age', 'time_in_hospital', 'num_lab_procedures', 'num_medications', 
                     'number_outpatient', 'number_emergency', 'number_inpatient', 'number_diagnoses']:
        user_inputs[feature] = st.number_input(f"{feature}:", min_value=0, value=0)
    else:
        user_inputs[feature] = st.text_input(f"{feature}:")

# Button to predict
if st.button("Predict Readmission"):
    # Convert user inputs to DataFrame
    input_data = pd.DataFrame([user_inputs])
    
    # Encode categorical features to match training format
    for col in categorical_features:
        input_data[col] = input_data[col].astype('category').cat.codes

    # Ensure correct feature order
    input_data = input_data[features]
    
    # Make predictions
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)
    
    # Display results
    st.subheader("Prediction Result")
    st.write(f"Readmission Prediction: {'Yes' if prediction[0] == 1 else 'No'}")
    st.write(f"Prediction Probabilities: {probabilities[0]}")

# Footer
st.sidebar.info("This app predicts the likelihood of readmission for diabetic patients.")
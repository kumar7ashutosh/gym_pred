import pickle,pandas as pd,numpy as np,streamlit as st
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title('calorie burn prediction')
gender = st.selectbox('Gender', ['Male', 'Female'])
age = int(st.number_input('Age'))
height = float(st.number_input('Height (cm)'))
weight = float(st.number_input('Weight (kg)'))
duration = float(st.number_input('Duration of Exercise (minutes)'))
heart_rate = float(st.number_input('Average Heart Rate (bpm)'))
body_temp = float(st.number_input('Body Temperature after Exercise (°C)'))
gender_encoded = 0 if gender == 'Male' else 1
input_data = pd.DataFrame([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]],
                          columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])
if st.button('Predict Calories Burned'):
    prediction = model.predict(input_data)[0]
    st.success(f"{prediction}")
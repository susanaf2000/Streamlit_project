# your code here
import pickle as pkl
import streamlit as st
import numpy as np

model_file = pkl.load(open('../models/random_forest_classifier_default_42.sav', 'rb'))

def diabetes_prediction(input_data): 
  
    # Changing the data into a NumPy array 
    input_data_as_nparray = np.asarray(input_data) 
  
    # Reshaping the data since there is only one instance 
    input_data_reshaped = input_data_as_nparray.reshape(1, -1) 
  
    prediction = model_file.predict(input_data_reshaped) 
  
    if prediction == 0: 
        return 'Non Diabetic'
    else: 
        return 'Diabetic'
  
def main(): 
  
    st.title('Diabetes Prediction') 
  
    Pregnancies = st.selectbox('No of pregnancies:', ['0', '1', '2', '3', '4', 'more']) 
    Glucose = st.text_input('Glucose level:') 
    BloodPressure = st.text_input('Blood Pressure value:') 
    SkinThickness = st.text_input('Skin thickness value:') 
    Insulin = st.text_input('Insulin level:') 
    BMI = st.text_input('BMI value:') 
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function value:') 
    Age = st.text_input('Age:') 
  
    diagnosis = '' 
  
    if st.button('Predict'): 
        diagnosis = diabetes_prediction( 
            [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]) 
  
    st.success(diagnosis) 
  
if __name__ == '__main__': 
    main()
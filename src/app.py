# your code here
import pickle
import streamlit as st

model_file = open('../models/decision_tree_classifier_default_42.sav', 'rb')
model = pickle.load(model_file)


st.title("Iris - Decision Tree prediction")

val1 = st.slider("Petal width", min_value = 0.0, max_value = 4.0, step = 0.1)
val2 = st.slider("Petal length", min_value = 0.0, max_value = 4.0, step = 0.1)
val3 = st.slider("Sepal width", min_value = 0.0, max_value = 4.0, step = 0.1)
val4 = st.slider("Sepal length", min_value = 0.0, max_value = 4.0, step = 0.1)

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4]])[0])
    st.write("Prediction:", prediction)

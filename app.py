import streamlit as st
import pandas as pd 
from dummies import * 
import joblib 

model=joblib.load('used_cars_model.h5')


st.title('Used Cars Streamlit App')
st.info('just building a testing app for our ml model ')


year=st.number_input('Enter The year of the car: ')
kilometers_driven=st.number_input('Enter the kilometers: ')
owner_type=st.slider('Owner? ',0,4,2)
engine=st.number_input('Enter the engine of the car: ')
power=st.number_input('Enter the power of the car: ')
seats=st.slider('Which Seats? ',2,8,4)
location_selection=st.selectbox('Select the location? ',['Bangalore','Chennai','Coimbatore','Delhi','Hyderabad','Jaipur','Kochi','Kolkata','Mumbai','Pune','Mumbai'])
location=location_dummies[location_selection]
fuel_type_Diesel=st.selectbox('fuel_type_Diesel or Not? ',[0,1])
transmission_Manual=st.selectbox('transmission_Manual or Not? ',[0,1])


data=[year,kilometers_driven,owner_type,engine,power,seats,fuel_type_Diesel,transmission_Manual]
data=data+location

st.write(data)


result=model.predict([data])

st.write(result)

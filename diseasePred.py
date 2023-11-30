# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:05:34 2023

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

heart_disease_model = pickle.load(open('heart_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          
                          ['Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex :1(Male),0(Female)')
        
    with col3:
        cp = st.text_input('Chest Pain types:values(0-3)')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl : 1(True) , 0(False)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results : values(0-2)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina :1(Yes) , 0(No)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment:values(0-2)')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy:values(0-3)')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

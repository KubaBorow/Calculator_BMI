import streamlit as st
import pandas as pd
import subprocess
import glob
from pathlib import Path

st.write('This app is to increase Your health.')

col1, col2 = st.columns(2)
try:
    var1 = col1.number_input('Enter your height in cm:', value=None, placeholder='Type a number')

    var2 = col2.number_input('Enter your weight in kg:', value=None, placeholder='Type a number')

    number = int(var2 / (var1 * var1 / 10000))

    st.write('Your score is', number)

    if number <= 25:
        st.write(""":green[Your BMI is good.]""")
    elif number < 30:
        st.write('You have class 1 obesity.')
    else:
        st.write('You need go to see a doctor immediately!')

except TypeError:
    st.write(""":red[Try another number !]""")

st.subheader("Type today`s information: ")

# with st.form(key='meal_form'):
#     col3, col4 = st.columns(2)
#     date = col3.text_input("Enter today`s date: ")
#     mood = col4.text_input("How do you rate your mood today from 1 to 10? ")
#
#     message = st.text_area(label="", placeholder="Enter your meals here...")
#
#     button = st.form_submit_button("Submit")
#     if button:
#         with open(f"{date}.txt, 'w") as file:
#             file.write(mood + 2 * '\n')
#             file.write(message)
#         st.info(""":green[Your information`s was stored successfully.]""")
with st.form('information_form'):
    st.header('information_form')

    col1, col2 = st.columns(2)
    with col1:

        mood = st.slider('Today`s mood', 0, 10)
    with col2:
        Date = st.date_input('Enter Date')

    submit_button = st.form_submit_button('Submit')

if st.form_submit_button:
    st.write('**Enter Date:**', Date,
             '**Mood:**', mood)



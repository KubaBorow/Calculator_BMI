import streamlit as st
from save_dir import path


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

with st.form('information_form'):
    st.header('Information Form')

    col1, col2 = st.columns(2)
    with col1:
        mood = st.slider('Today`s mood', 0, 10)
    with col2:
        date = st.date_input('Enter Date')

    meals = st.text_area(label="Enter your meals")
    st.write('**Enter Date:**', date,
             '**Mood:**', mood)

    submit_button = st.form_submit_button('Submit')

if submit_button:
    with open(f'{path}{date}.txt', 'w') as file:
        file.write(f'Today`s date is: {str(date)}' + 1 * '\n')
        file.write(f'Your mood for today is: {str(mood)}.' + 2 * '\n')
        file.write('Today in your menu was:\n'f"{meals}")
        st.info(""":green[Your information was stored successfully.]""")
else:
    st.info(""":red[Your information`s file wasn`t created.]""")

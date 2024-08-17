import streamlit as st
import functions
import time


st.set_page_config(
    page_title="Calculator"
)
# theme[]

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.write('This app is to increase Your health.')

col1, col2 = st.columns(2)
try:
    var1 = col1.number_input('Enter your height in cm:', value=None, placeholder='Type a number')

    var2 = col2.number_input('Enter your weight in kg:', value=None, placeholder='Type a number')

    number = int(var2 / (var1 * var1 / 10000))

    st.write('Your score is', number)

    if number <= 25:
        st.write('Your BMI is good.')
    elif number < 30:
        st.write('You have class 1 obesity.')
    else:
        st.write('You need go to see a doctor.')

except TypeError:
    st.write('Try another number')

col3, col4 = st.columns(2)
col3.text_input("Enter today`s date: ")
col4.text_input("How do you rate your mood today from 1 to 10? ")
st.subheader("Add your meals under: ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=' ', placeholder='Add meals...',
              on_change=add_todo, key='new_todo')

# save_btn = st.button('Save', type='secondary')

# if save_btn:
#     with st.spinner('Saving...'):
#         time.sleep(3)
    # with open(f'../journal/{date}.txt', 'w') as file:
    # file.write(mood + 2 * '\n')
    # file.write(thoughts)

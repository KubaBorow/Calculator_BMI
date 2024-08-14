import streamlit as st
import functions

# theme[]

todos = functions.get_todos()


# number = functions.caculator(weight='kg', height='cm')


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My BMI Calculator")
st.subheader("This is my BMI calculator.")
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

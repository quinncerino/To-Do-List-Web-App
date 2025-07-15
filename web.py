import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + '\n')
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My To-Do List")
st.subheader("This is your own personal to-do list!")
st.write("This app's purpose is to increase your <b>productivity</b>.", unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ", label_visibility="collapsed", placeholder="Add a new task...", key='new_todo', on_change = add_todo)


#st.session_state
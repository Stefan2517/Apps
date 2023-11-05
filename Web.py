# ca sa rulez scriu in terminal: streamlit run Web.py
# ordinea liniilor de cod conteaza pt streamlit in ceea ce priveste alcatuirea paginii web
import streamlit as st
import Functii

todos = Functii.get_activitati()
def add_activitate():
    activitate = st.session_state["new_todo"] + "\n"
    todos.append(activitate)
    Functii.write_activitati(todos)

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functii.write_activitati(todos)
        del st.session_state[todo]
        st.experimental_rerun()


#la label daca scriam cv aparea deasupra casutei
st.text_input(label="", label_visibility="hidden", placeholder="Scrie o activitate...",
              on_change=add_activitate, key="new_todo")

#print("Hello")

#st.session_state #ne zice daca e false sau true activitatile afisate. True e daca casuta e bifata pt activitate!
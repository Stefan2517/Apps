# ca sa rulez scriu in terminal: streamlit run Web.py
# ordinea liniilor de cod conteaza pt streamlit in ceea ce priveste alcatuirea paginii web
import streamlit as st
import Functii

todos = Functii.get_activitati()

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Scrie o activitate...") #la label daca scriam cv aparea deasupra casutei


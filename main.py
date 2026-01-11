import streamlit as st
from io import StringIO

st.title("Schedule Lynx")
st.write("Welcome to Schedule Lynx! Upload your person.json files to get started.")



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    with open(uploaded_file, 'r') as file:
        COLORS = [tuple(color) for color in list(st.json.load(file).values())]
    st.write(COLORS)
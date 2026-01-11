import streamlit as st
import json

st.title("Schedule Lynx")
st.write("Welcome to Schedule Lynx! Upload your person.json files to get started.")

# 1. Create the file uploader widget
# type='json' restricts the user to selecting only .json files
uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

# 2. Check if a file has been uploaded
if uploaded_file is not None:
    try:
        # 3. Load the JSON data
        # Streamlit's file_uploader returns a file-like object, 
        # so we can simply pass it to json.load()
        data = json.load(uploaded_file)
        
        # 5. Display the data
        # st.json() creates an interactive, collapsible view of the data
        st.subheader(uploaded_file.name)
        st.json(data)
        
        # You can now access data as a standard Python dictionary/list
        # Example: st.write(data['some_key'])
        
    except json.JSONDecodeError:
        st.error("The file you uploaded is not valid JSON.")
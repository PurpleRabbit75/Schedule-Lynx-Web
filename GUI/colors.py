import streamlit as st
import json

st.title("Colors")


uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])


with open('config/colors.json', 'r') as file:
    data = json.load(file)
    display = st.json(data)


# 2. Check if a file has been uploaded
if uploaded_file is not None:
    try:
        # 3. Load the JSON data
        # Streamlit's file_uploader returns a file-like object, 
        # so we can simply pass it to json.load()
        data = json.load(uploaded_file)
        
        # 4. Success message
        st.success("JSON loaded successfully!")
        
        del display
        display = st.json(data)

        with open("config/colors.json", "w") as f:
            json.dump(data, f)
        
    except json.JSONDecodeError:
        st.error("The file you uploaded is not valid JSON.")

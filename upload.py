import streamlit as st
import json

st.title("Schedule Lynx")
st.write("Welcome to Schedule Lynx! Upload up to 12 person.json files to get started.")

num_uploads = st.slider("Enter the total number of schedules", 2, 12)

# Check if 'user_data_array' exists, if not, initialize it
if 'user_data_array' not in st.session_state:
    st.session_state['user_data_array'] = []
if 'user_data_file_names' not in st.session_state:
    st.session_state['user_data_file_names'] = []

for i in range(num_uploads):
    # 1. Create the file uploader widget
    # type='json' restricts the user to selecting only .json files
    uploaded_file = st.file_uploader("", type=["json"], key = i)

    # 2. Check if a file has been uploaded
    if uploaded_file is not None:
        try:
            # 3. Load the JSON data
            # Streamlit's file_uploader returns a file-like object, 
            # so we can simply pass it to json.load()
            data = json.load(uploaded_file)
            st.session_state['user_data_array'].append(data)
            st.session_state['user_data_file_names'].append(uploaded_file.name)
            
            # 4. Success message
            st.success("JSON loaded successfully!")
            
            
            
            # You can now access data as a standard Python dictionary/list
            # Example: st.write(data['some_key'])
            
        except json.JSONDecodeError:
            st.error("The file you uploaded is not valid JSON.")




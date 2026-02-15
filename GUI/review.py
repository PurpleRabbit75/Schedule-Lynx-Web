import streamlit as st

st.title("Review the files you uploaded...")
# 5. Display the data
        # st.json() creates an interactive, collapsible view of the data
#st.subheader(uploaded_file.name)
for i in range(len(st.session_state['user_data_array'])):
    st.subheader(st.session_state['user_data_file_names'][i])
    st.json(st.session_state['user_data_array'][i])
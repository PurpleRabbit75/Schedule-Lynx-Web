import streamlit as st

# st.title("Schedule Lynx")

pages = {
    "Main App": [
        st.Page("upload.py", title="Upload Files"),
        st.Page("review.py", title="Review Uploads"),
        st.Page("download.py", title="Download Schedule"),
    ],
    "Settings": [
        st.Page("config.py", title="Configuration"),
        st.Page("colors.py", title="Colors"),
    ],
}

pg = st.navigation(pages)
pg.run()
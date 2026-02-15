import streamlit as st

pages = {
    "Main App": [
        st.Page("GUI/upload.py", title="Upload Files"),
        st.Page("GUI/review.py", title="Review Uploads"),
        st.Page("GUI/download.py", title="Download Schedule"),
    ],
    "Settings": [
        st.Page("GUI/config.py", title="Configuration"),
        st.Page("GUI/colors.py", title="Colors"),
    ],
}

pg = st.navigation(pages)
pg.run()
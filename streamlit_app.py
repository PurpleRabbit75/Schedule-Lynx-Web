import streamlit as st

# st.title("Schedule Lynx")

pages = {
    "Main App": [
        st.Page("main.py", title="Schedule Lynx"),
    ],
    "Settings": [
        st.Page("config.py", title="Configuration"),
        st.Page("colors.py", title="Colors"),
    ],
}

pg = st.navigation(pages)
pg.run()
import streamlit as st
from backend_api import main

st.title("Download Page")
st.image("https://raw.githubusercontent.com/PurpleRabbit75/Schedule-Lynx/d5f241a72e99fbb101ff0fe21500815619a1cfa1/Miscellaneous-Developer-Stuff/Schedule-Lynx-icon.png", width=250, output_format="PNG")
img, WIDTH = main()
st.image(img, width = WIDTH, output_format="PNG")
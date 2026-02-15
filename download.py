import streamlit as st
from backend_api import main

st.title("Download Page")
st.image("https://raw.githubusercontent.com/PurpleRabbit75/Schedule-Lynx/d5f241a72e99fbb101ff0fe21500815619a1cfa1/Miscellaneous-Developer-Stuff/Schedule-Lynx-icon.png", width=800, output_format="PNG")

st.image(main())


# IndexError: string index out of range

# File "C:\Users\abrah\Documents\GitHub\Schedule-Lynx-Web\streamlit_app.py", line 18, in <module>
#     pg.run()
#     ~~~~~~^^
# File "C:\Users\abrah\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\streamlit\navigation\page.py", line 310, in run
#     exec(code, module.__dict__)  # noqa: S102
#     ~~~~^^^^^^^^^^^^^^^^^^^^^^^
# File "C:\Users\abrah\Documents\GitHub\Schedule-Lynx-Web\download.py", line 7, in <module>
#     st.image(main())
#              ~~~~^^
# File "C:\Users\abrah\Documents\GitHub\Schedule-Lynx-Web\backend_api.py", line 249, in main
#     write_to_image(i)
#     ~~~~~~~~~~~~~~^^^
# File "C:\Users\abrah\Documents\GitHub\Schedule-Lynx-Web\backend_api.py", line 143, in write_to_image
#     add_time_block(name, data[i][0], data[i][1], data[i][2])
#                                      ~~~~~~~^^^
# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import streamlit.components.v1 as components
import hmac
# from streamlit_dimensions import st_dimensions as dim

# def check_password():
#     """Returns `True` if the user had the correct password."""

#     def password_entered():
#         """Checks whether a password entered by the user is correct."""
#         if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
#             st.session_state["password_correct"] = True
#             del st.session_state["password"]  # Don't store the password.
#         else:
#             st.session_state["password_correct"] = False

#     # Return True if the passward is validated.
#     if st.session_state.get("password_correct", False):
#         return True

#     # Show input for password.
#     st.text_input(
#         "Password", type="password", on_change=password_entered, key="password"
#     )
#     if "password_correct" in st.session_state:
#         st.error("😕 Password incorrect")
#     return False


# if not check_password():
#     st.stop()  # Do not continue if check_password is not True.

def run():
  st.set_page_config(
      page_title="Edge Inn Schedule",
      layout='wide'
  )

  # Add custom CSS to hide the toolbar items at the top of the page  
  hide_toolbar_items = """
  <style>
  #MainMenu {visibility: hidden;}
  #GithubIcon {visibility: hidden;}
  </style>
  """
  st.markdown(hide_toolbar_items, unsafe_allow_html=True)

  col1, col2, col3 = st.columns([0.01, 0.98, 0.01])

  with col2:
    iframe_src="https://calendar.google.com/calendar/embed?wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&src=ZjViOThjYWJjZDAzY2Y0ZmFkZjk4ZjM1NDNlYWNjNzQyNjVjNTFmYzZjMTRhNTkzNjExNjk4MGM4ODhiMWU0Y0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23D50000"
    # dim_output = dim(key='col2')
    # width = dim_output["width"]
    # components.iframe(iframe_src, width=width, height= width*0.7, scrolling=True)
    components.iframe(iframe_src, width=800, height= 600, scrolling=True)


if __name__ == "__main__":
    run()

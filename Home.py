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
from streamlit_dimensions import st_dimensions as dim

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
    iframe_src="https://calendar.google.com/calendar/embed?wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&src=ZjA2MTc0MmYzZTMxNjMxMzdjNjNmYzQ3NzUzMWI5MTBkNDFkZGYxMGNjMzFjYmY0MTNjY2VmZTNmNmI0ZGU1MUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23B39DDB"
    dim_output = dim(key='col2')
    width = dim_output["width"]
    components.iframe(iframe_src, width=width, height= width*0.7, scrolling=True)


if __name__ == "__main__":
    run()

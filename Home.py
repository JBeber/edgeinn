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
import streamlit.components.v1 as components

def run():
    st.set_page_config(
        page_title="Edge Inn Schedule",
    )

    iframe_src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&src=ZjA2MTc0MmYzZTMxNjMxMzdjNjNmYzQ3NzUzMWI5MTBkNDFkZGYxMGNjMzFjYmY0MTNjY2VmZTNmNmI0ZGU1MUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23B39DDB"
    components.iframe(iframe_src, width=800, height=600)


if __name__ == "__main__":
    run()

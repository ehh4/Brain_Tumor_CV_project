import streamlit as st
import pandas as pd
from ultralytics import YOLO


class page2:
    def __init__(self) -> None:
        pass

    def __hideHeader__(self) -> None:
        hide_decoration_bar_style = '''
            <style>
                header {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    def renderPage2(self) -> None:
        self.__hideHeader__()
        st.write("PAGE 2")
        st.write("Brain Tumor Prediction Page")
        url = "https://www.streamlit.io"
        st.write("check out this [link](%s)" % url)
        st.markdown("check out this [link](%s)" % url)
        pass

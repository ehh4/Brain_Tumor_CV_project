import streamlit as st
import pandas as pd
from ultralytics import YOLO
from style import st_style


class page2:
    def __init__(self) -> None:
        pass


    def renderPage2(self) -> None:
        st_style.config_page(page_title="Brain Tumor Prediction", page_icon="✨")
        st_style.hide_header()
        st.write("PAGE 2")
        st.write("Brain Tumor Prediction Page")
        url = "https://www.streamlit.io"
        st.write("check out this [link](%s)" % url)
        st.markdown("check out this [link](%s)" % url)
        pass

if __name__ == "__main__":
    page_2 = page2()
    page_2.renderPage2()
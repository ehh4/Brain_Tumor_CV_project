""" Custom Style for streamlit. """
import streamlit as st


class CustomStyle:
    """ st_style class for streamlit. """
    def config_page(self, page_title, page_icon):
        """ Config streamlit interface. """
        st.set_page_config(
            page_title = page_title,
            page_icon = page_icon
        )


    def hide_header(self):
        """ Hide ugly streamlit header. """
        hide_decoration_bar_style = '''
        <style>
            header {visibility: hidden;}
        </style>
        '''
        st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

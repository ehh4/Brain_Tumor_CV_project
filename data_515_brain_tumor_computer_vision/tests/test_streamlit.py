"""test_streamlit.py"""
import unittest
import streamlit as st
from streamlit.testing.v1 import AppTest


class TestStreamlit(unittest.TestCase):
    def test_landing_page(self):
        """ Test landing page displays brain info markdowns """
        at = AppTest.from_file("ui_demo/brain_tumor_information.py").run()
        # st.title and st.markdown
        assert len(at.markdown) == 8


    def test_prediction_page(self):
        """ Test brain prediction page displays relevant info """
        at = AppTest.from_file("ui_demo/pages/brain_tumor_prediction.py").run()
        # st.title and st.markdown
        assert len(at.markdown) == 3


    def test_bot(self):
        """ Test bot interface"""
        at = AppTest.from_file("ui_demo/pages/infobot.py").run()
        assert len(at.button) == 4

""" test_streamlit.py includes all streamlit app testing """
import unittest
from streamlit.testing.v1 import AppTest


class TestStreamlit(unittest.TestCase):
    """ Streamlit app test class. """
    def test_landing_page(self):
        """ Test landing page displays brain info markdowns """
        at = AppTest.from_file("ui_demo/Brain_Tumor_Information.py").run()
        # st.title and st.markdown
        assert len(at.markdown) == 8


    def test_prediction_page(self):
        """ Test brain prediction page displays relevant info """
        at = AppTest.from_file("ui_demo/pages/Brain_Tumor_Prediction.py").run()
        # st.title and st.markdown
        assert len(at.markdown) == 3


    def test_bot(self):
        """ Test bot interface"""
        at = AppTest.from_file("ui_demo/pages/infobot.py").run()
        assert len(at.button) == 4


    def test_render_infobot(self):
        """ Test bot interface"""
        at = AppTest.from_file("ui_demo/pages/infobot.py").run()
        assert len(at.markdown) == 2

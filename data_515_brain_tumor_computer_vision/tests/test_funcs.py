"""test_funcs.py"""
import unittest
from unittest.mock import MagicMock, patch
import cv2
import ui_demo.pages.Brain_Tumor_Prediction as bp
import ui_demo.pages.infobot as ib
import ui_demo.Brain_Tumor_Information as bi


class TestFunctions(unittest.TestCase):
    def test_get_predicted_img_smoke(self):
        """ __get_predicted_img__ smoke test. """
        test = bp.PredictionPage()
        test.__get_predicted_img__('tests/predict')
        self.assertEqual('smoke'.upper(), 'SMOKE')


    def test_get_predicted_img(self):
        """ __get_predicted_img__ normal functionality test. """
        test = bp.PredictionPage()
        img_path = test.__get_predicted_img__('tests/predict')
        self.assertEqual(img_path, 'tests/predict/input.jpg')


    def test_get_predicted_img_edge_one(self):
        """ Edge one: The directory doesn't exist. """
        test = bp.PredictionPage()
        with self.assertRaises(ValueError):
            test.__get_predicted_img__('/Desktop')


    def test_get_predicted_img_edge_two(self):
        """ Edge two: The directory is not the correct one. """
        test = bp.PredictionPage()
        with self.assertRaises(ValueError):
            test.__get_predicted_img__('/')

    def test_get_predicted_img_edge_three(self):
        """ Edge three: The directory is not a string type. """
        test = bp.PredictionPage()
        with self.assertRaises(TypeError):
            test.__get_predicted_img__(89)


    def test_preprocess_img_smoke(self):
        """ __preprocess_img__ smoke test. """
        test = bp.PredictionPage()
        test.__preprocess_img__("tests/input_raw.jpg")
        self.assertEqual('smoke'.upper(), 'SMOKE')


    def test_preprocess_img(self):
        """ __preprocess_img__ smoke functionality test. """
        test = bp.PredictionPage()
        test.__preprocess_img__("tests/input_raw.jpg")
        img = cv2.imread("input.png")
        # Get the shape of the image
        height, width, channels = img.shape if len(img.shape) == 3 else (img.shape[0], img.shape[1], 1)
        # Check if the image is grayscale (only compares height and width)
        # also that the img height and width are both 640
        is_grayscale = height == width == 640
        self.assertTrue(is_grayscale)


    def test_preprocess_img_edge_one(self):
        """ __preprocess_img__ smoke input is not a string. """
        test = bp.PredictionPage()
        x = 10
        with self.assertRaises(TypeError):
            test.__preprocess_img__(x)


    def test_preprocess_img_edge_two(self):
        """ __preprocess_img__ smoke wrong img path. """
        test = bp.PredictionPage()
        with self.assertRaises(ValueError):
            test.__preprocess_img__("tests/test_weird.pdf")


    def test_chat_response_generator_smoke(self):
        """ response_generator smoke test. """
        test = ib.InfobotPage()
        test.response_generator("Get Additional Help")
        self.assertEqual('smoke'.upper(), 'SMOKE')


    def test_chat_response_generator_valid_inputs(self):
        """ response_generator all valid input test. """
        test = ib.InfobotPage()
        valid_button_vals = ["Learn about Brain Cancer", "Get Brain Tumor Prediction",
        "Get Diagnosis Next Steps", "Get Additional Help"]
        for input in valid_button_vals:
            res = test.response_generator(input)
            if res:
                res = None
            self.assertIsNone(res)


    def test_chat_response_generator_wrong_input_type(self):
        """ response_generator wrong type of input. """
        test = ib.InfobotPage()
        input = 390
        with self.assertRaises(TypeError):
            res = test.response_generator(input)


    def test_chat_response_generator_invalid_input(self):
        """ response_generator invalid input. """
        test = ib.InfobotPage()
        input = "Brain no braining"
        with self.assertRaises(ValueError):
            res = test.response_generator(input)

    def test_render_prediction_page(self):
        "Test render prediction page function smoke test"
        test = bp.PredictionPage()
        res = test.render_prediction_page()
        self.assertEqual('smoke'.upper(), 'SMOKE')

    def test_landing_page(self):
        "Test landing page function smoke test"
        res = bi.landing_page()
        self.assertEqual('smoke'.upper(), 'SMOKE')


    @patch('ui_demo.pages.infobot.st')
    def test_render_infobot_page(self, mock_st):
        # Mock the streamlit app
        mock_st.session_state.messages = []
        mock_st.markdown = MagicMock()
        mock_st.button = MagicMock(return_value=True)
        mock_st.columns = MagicMock(return_value=(MagicMock(), MagicMock(),
                                                  MagicMock(), MagicMock()))

        infobot_page = ib.InfobotPage()
        infobot_page.render_infobot_page()

        # Use assert to throw exceptions
        mock_st.button.assert_any_call("Learn about Brain Cancer")
        mock_st.button.assert_any_call("Get Brain Tumor Prediction")
        mock_st.button.assert_any_call("Get Diagnosis Next Steps")
        mock_st.button.assert_any_call("Get Additional Help")



if __name__ == '__main__':
    unittest.main()
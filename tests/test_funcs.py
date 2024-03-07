"""test_funcs.py"""
import unittest
import cv2
import ui_demo.pages.Brain_Tumor_Prediction as bp


class TestFunctions(unittest.TestCase):
    def test_get_predicted_img_smoke(self):
        """ __get_predicted_img__ smoke test. """
        test = bp.Page2()
        test.__get_predicted_img__('tests/predict')
        self.assertEqual('smoke'.upper(), 'SMOKE')


    def test_get_predicted_img(self):
        """ __get_predicted_img__ normal functionality test. """
        test = bp.Page2()
        img_path = test.__get_predicted_img__('tests/predict')
        self.assertEqual(img_path, 'tests/predict/input.jpg')


    def test_get_predicted_img_edge_one(self):
        """ Edge one: The directory doesn't exist. """
        test = bp.Page2()
        with self.assertRaises(ValueError):
            test.__get_predicted_img__('/Desktop')


    def test_get_predicted_img_edge_two(self):
        """ Edge two: The directory is not the correct one. """
        test = bp.Page2()
        with self.assertRaises(ValueError):
            test.__get_predicted_img__('/')


    def test_preprocess_img_smoke(self):
        """ __preprocess_img__ smoke test. """
        test = bp.Page2()
        test.__preprocess_img__("tests/input_raw.jpg")
        self.assertEqual('smoke'.upper(), 'SMOKE')


    def test_preprocess_img(self):
        """ __preprocess_img__ smoke functionality test. """
        test = bp.Page2()
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
        test = bp.Page2()
        x = 10
        with self.assertRaises(TypeError):
            test.__preprocess_img__(x)


    def test_preprocess_img_edge_two(self):
        """ __preprocess_img__ smoke wrong img path. """
        test = bp.Page2()
        with self.assertRaises(ValueError):
            test.__preprocess_img__("tests/test_weird.pdf")


if __name__ == '__main__':
    unittest.main()
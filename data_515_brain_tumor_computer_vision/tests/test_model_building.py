"""test_funcs.py"""
import unittest
from unittest.mock import MagicMock, patch
import cv2
from model_training import model_building


class TestModels(unittest.TestCase):
    def test_build_model_is_scan(self):
        """
        Smoke test to create model that
        determines if image is brain scan
        
        Returns the created model to:
        runs/classify/is_brain_scan_test
        """
        model_building.train_is_brain_scan_model(
            "model_training/yolov8n-cls.pt",
            "model_training/sample_data/is_scan_data",
            "is_brain_scan_test")
        self.assertEqual('smoke'.upper(), 'SMOKE')

    def test_build_model_is_tumor(self):
        """
        Smoke test to create model that
        determines if brain scan contains tumor
        
        Returns the created model to:
        runs/classify/is_tumor_test
        """
        model_building.train_is_tumor_model(
            "model_training/yolov8n-cls.pt",
            "model_training/sample_data/is_tumor",
            "is_tumor_test")
        self.assertEqual('smoke'.upper(), 'SMOKE')


if __name__ == '__main__':
    unittest.main()
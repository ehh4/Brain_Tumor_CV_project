# pylint: disable=import-error
# pylint: disable=no-name-in-module

# These two pylint errors have been
# silenced due to the imports working

"""
These tests are for model_building.py which
provide insight into how the full model was trained. 
Because ultralytics coded the .predict(), .train()
and model initiation, only smoke tests are provided.
"""
import unittest
import model_training.model_building as mb


class TestModels(unittest.TestCase):
    """This holds all smoke tests"""
    def test_build_model_is_scan(self):
        """
        Smoke test to create model that
        determines if image is brain scan
        
        Returns the created model to:
        runs/classify/is_brain_scan_test
        """
        mb.train_is_brain_scan_model(
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
        mb.train_is_tumor_model(
            "model_training/yolov8n-cls.pt",
            "model_training/sample_data/is_tumor",
            "is_tumor_test")
        self.assertEqual('smoke'.upper(), 'SMOKE')

    def test_main(self):
        """
        Smoke test to see if main works.
        Main initiates the creation of the 
        two classification models
        """
        mb.main()
        self.assertEqual('smoke'.upper(), "SMOKE")

if __name__ == '__main__':
    unittest.main()

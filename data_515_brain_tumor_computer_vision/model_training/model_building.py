"""
The code below are examples of how to train the models used in our project.
The epochs and batch size are intentionally reduced to be compatible
with the subset of training data uploaded.
The real models utilize larger datasets, more epochs, and larger batch sizes.
"""

from ultralytics import YOLO



def train_is_brain_scan_model(prebuilt_model, data_folder):
    """
    Trains a model that predicts whether a given image is a brain scan
    Parameters:
        - prebuilt_model: A Yolov8 pre-trained model to start with. 
        Must be a .pt file. Provided in the models folder
        - data_folder: Path to directory where the training, testing,
        and validation data is stored
    Saves the model weights and metadata to runs/classify/is_brain_scan
    """
    model = YOLO(prebuilt_model)
    model.train(
        data=data_folder, epochs=1, batch=3, imgsz=640,
        name="is_brain_scan")

def train_is_tumor_model(prebuilt_model, data_folder):
    """
    Trains a model that predicts whether a given brain scan has a tumor
    Parameters:
        - prebuilt_model: A Yolov8 pre-trained model to start with.
        Must be a .pt file. Provided in the models folder
        - data_folder: Path to directory where the training, testing,
        and validation data is stored
    Saves the model weights and metadata to runs/classify/is_tumor
    """
    model = YOLO(prebuilt_model)
    model.train(
        data=data_folder, epochs=1, batch=3, imgsz=640,
        name="is_tumor")

def train_locate_tumor_model(prebuilt_model, yaml_file):
    """
    Trains a model that predicts the location for the given brain scan
    Parameters:
        - prebuilt_model: A Yolov8 pre-trained model to start with.
        Must be a .pt file. Provided in the models folder
        - yaml_file: Path to .yaml file that indexes the 
        images and their masks. 
    Saves the model weights and metadata to runs/classify/locate_tumor
    """
    # model saved to runs/segment
    model = YOLO(prebuilt_model)
    model.train(
        data=yaml_file, epochs=1, batch=3, imgsz=640,
        name="locate_tumor")

def main():
    """
    Runs all three models and saves the best weights 
    and metadata to respective folders
    """
    train_is_brain_scan_model(
        "model_training/yolov8n-cls.pt",
        "model_training/sample_data/is_scan_data")
    train_is_tumor_model(
        "model_training/yolov8n-cls.pt",
        "model_training/sample_data/is_tumor")
    train_locate_tumor_model(
        "model_training/yolov8n-seg.pt",
        "model_training/sample_data/locate_tumor/data.yaml")

if __name__ == "__main__":
    main()

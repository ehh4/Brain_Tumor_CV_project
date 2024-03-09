"""
The code below are examples of how to train the models used in our project.
The epochs and batch size are intentionally reduced to be compatible
with the subset of training data uploaded.
The real models utilize larger datasets, more epochs, and larger batch sizes.
"""

from ultralytics import YOLO



def train_is_brain_scan_model(prebuilt_model, data_folder):
    """test123"""
    # model saved to runs/classify/is_brain_scan
    model = YOLO(prebuilt_model)
    model.train(
        data=data_folder, epochs=1, batch=3, imgsz=640,
        name="is_brain_scan")

def train_is_tumor_model(prebuilt_model, data_folder):
    """test123"""
    # model saved to runs/classify/is_tumor
    model = YOLO(prebuilt_model)
    model.train(
        data=data_folder, epochs=1, batch=3, imgsz=640,
        name="is_tumor")

def train_locate_tumor_model(prebuilt_model, yaml_file):
    """test123"""
    # model saved to runs/segment
    model = YOLO(prebuilt_model)
    model.train(
        data=yaml_file, epochs=1, batch=3, imgsz=640,
        name="locate_tumor")

def main():
    """test123"""
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

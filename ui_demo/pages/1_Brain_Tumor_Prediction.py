import os
import cv2
import streamlit as st
import pandas as pd


from ultralytics import YOLO
from style import st_style
from io import BytesIO



class page2:
    def __init__(self) -> None:
        self.MODEL_locate_tumor = 'models/locate_tumor/weights/best.pt'
        self.MODEL_is_scan = 'models/is_scan/weights/best.pt'
        self.MODEL_is_tumor = "models/is_tumor/weights/best.pt"
    
    
    def getPredictedImg(self, result_dir) -> str:
        img_path = str(result_dir) + "/"
        filenames = os.listdir(result_dir)
        for f in filenames:
            img_path += str(f)
        return img_path

    
    def preprocessImg(self) -> None:
        img = cv2.imread("input.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (640, 640), interpolation = cv2.INTER_AREA)
        cv2.imwrite("input.png", img)
        


    def renderPage2(self) -> None:

        st_style.config_page(page_title="Brain Tumor Prediction", page_icon="✨")
        st.title("Brain Tumor Prediction Tool")
        st_style.hide_header()
        st.write("""About: This tool is equipped to analyze brain scan images and predict the tumor region (if there is one) and severity. 
                 To use, upload a brain scan image. Currently accepted filetypes: png, jpg, tiff.""")
        upload_img = st.file_uploader("Choose an image")
        # ADD IN code to reject non-images
        if upload_img is not None:
            file_extension = os.path.splitext(upload_img.name)[1].lower()
            if file_extension not in ['.jpg', '.jpeg', '.png', '.tiff', '.tif']:
                st.write("Unsupported file format. Please upload a JPEG, PNG, or TIFF image.")
                return
            else:
                # read img as bytes:
                bytes_data = upload_img.getvalue()
                bytesio_object = BytesIO(bytes_data)

                # save the img as png
                with open("input.png", "wb") as f:
                    f.write(bytesio_object.getbuffer())
                
                # grayscale and resize to 640 * 640
                self.preprocessImg()

                # determines if image is brain scan
                is_scan_model = YOLO(self.MODEL_is_scan)
                scan_results = is_scan_model.predict(source='input.png', save=True)
                print(scan_results[0].probs.top1)
                print(scan_results[0].probs.top1conf.item())
                if (scan_results[0].probs.top1 == 1) & (scan_results[0].probs.top1conf.item() > 0.8):
                    is_tumor_model = YOLO(self.MODEL_is_tumor)
                    tumor_results = is_tumor_model.predict(source='input.png', save=True)
                    if (tumor_results[0].probs.top1 == 1) & (tumor_results[0].probs.top1conf.item() > 0.7):
                        locate_tumor_model = YOLO(self.MODEL_locate_tumor)
                        location_results = locate_tumor_model.predict(source='input.png', save=True)
                        # run locate tumor model
                        result_dir = location_results[0].save_dir
                        img_path = self.getPredictedImg(result_dir)
                        st.write(img_path)
                        st.image(img_path)
                        st.write("Bad news, probably a tumor :(")
                        return
                    else:
                        st.write("Based on the current model, we don't believe there's a tumor in this brain scan")
                        return
                else:
                    st.write("Unfortunately, this image is not recognized as a brain scan. Please double-check to ensure you've uploaded a suitable brain scan image")
                    return



if __name__ == "__main__":
    page_2 = page2()
    page_2.renderPage2()
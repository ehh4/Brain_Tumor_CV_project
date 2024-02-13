import os
import cv2
import streamlit as st
import pandas as pd


from ultralytics import YOLO
from style import st_style
from io import BytesIO



class page2:
    def __init__(self) -> None:
        self.MODEL = '/opt/homebrew/runs/segment/train4/weights/best.pt'
    
    
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
        st_style.hide_header()
        st.write("Brain Tumor Prediction Page")
        upload_img = st.file_uploader("Choose an image")
        if upload_img is not None:
            # read img as bytes:
            bytes_data = upload_img.getvalue()
            bytesio_object = BytesIO(bytes_data)

            # save the img as png
            with open("input.png", "wb") as f:
                f.write(bytesio_object.getbuffer())
            
            # grayscale and resize to 640 * 640
            self.preprocessImg()

            model = YOLO(self.MODEL)
            results = model.predict(source='input.png', save=True)
            result_dir = results[0].save_dir
            img_path = self.getPredictedImg(result_dir)
            st.write(img_path)
            st.image(img_path)


if __name__ == "__main__":
    page_2 = page2()
    page_2.renderPage2()
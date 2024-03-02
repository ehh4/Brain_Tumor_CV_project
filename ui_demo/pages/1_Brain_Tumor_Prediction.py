"""
Brain Tumor Prediction page. Users can upload a brain CT image and get a predicted tumor severity image back.
    getPredictedImg: result_dir is where the predicted img is saved; returns the full img_path.
    preprocessImg: returns the grayscaled img of size 640 * 640.
    render_page2: displays the brain tumor prediction page.
"""
import os
import cv2
import streamlit as st
import pandas as pd


from ultralytics import YOLO
from style import st_style
from io import BytesIO



class page2:
    def __init__(self) -> None:
        self.MODEL = 'train4/weights/best.pt'


    def get_predicted_img(self, result_dir) -> str:
        """ Returns predicted img. """
        img_path = str(result_dir) + "/"
        filenames = os.listdir(result_dir)
        for f in filenames:
            img_path += str(f)
        return img_path


    def preprocess_img(self) -> None:
        """ Resize img to 640 * 640 and grayscaled the img before prediction. """
        img = cv2.imread("input.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (640, 640), interpolation = cv2.INTER_AREA)
        cv2.imwrite("input.png", img)


    def render_page2(self) -> None:
        """ Renders Brain Tumor Prediction page in streamlit. """
        st_style.config_page(page_title="Brain Tumor Prediction", page_icon="✨")
        st.markdown("<h1 style='text-align: center;'>Brain Tumor Prediction Page</h1>", unsafe_allow_html=True)
        st.markdown("""<p style='font-size: 20px;'>
                    <b>⚠️ Important Reminder: Medical Prediction Tool</b> <br>
                    Dear Users,<br>
                    Our Brain Tumor Prediction tool offers suggestions based on input data. It is not a substitute for professional medical advice.<br>
                    <br>
                    <b>👨‍⚕️ Seek Professional Help:</b> <br>
                    For related health concerns, consult a licensed healthcare provider. They can provide accurate, personalized advice based on your specific situation.<br>
                    <br>
                    <b> ❗️ Use Responsibly: </b> <br>
                    Our tool supports, but doesn't replace professional care. Don't delay seeking medical advice based solely on tool suggestions.<br>
                    Your health matters most. Use our tool as a guide, not a diagnosis.<br>
                    <br>
                    <br>
                    Please upload your brain CT image in the file uploader below by clicking on the "Browse Files" button. Thank you for using our tool!
                    </p>""",
                    unsafe_allow_html=True)

        upload_img = st.file_uploader("Upload image in format: .jpg, .jpeg, .png, .tiff, .tif")
        if upload_img is not None:
            # read img as bytes:
            bytes_data = upload_img.getvalue()
            bytesio_object = BytesIO(bytes_data)

            # save the img as png
            with open("input.png", "wb") as f:
                f.write(bytesio_object.getbuffer())

            # grayscale and resize to 640 * 640
            self.preprocess_img()

            model = YOLO(self.MODEL)
            results = model.predict(source='input.png', save=True)
            result_dir = results[0].save_dir
            img_path = self.get_predicted_img(result_dir)
            st.write(img_path)
            st.image(img_path)


if __name__ == "__main__":
    page_2 = page2()
    page_2.render_page2()

# pylint: disable=no-member
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-locals
# pylint: disable=invalid-name
# pylint: disable=import-error
"""
Brain Tumor Prediction page. 
Users can upload a brain CT image and get a predicted tumor severity image back.
    getPredictedImg: result_dir is where the predicted img is saved; returns the full img_path.
    preprocessImg: returns the grayscaled img of size 640 * 640.
    render_page2: displays the brain tumor prediction page.
"""
import os
from io import BytesIO
import cv2
import streamlit as st
from ultralytics import YOLO
from ui_demo.style import CustomStyle


class Page2:
    """ Brain Prediction Page Class. """
    def __init__(self) -> None:
        self.mod_loc_t = 'models/locate_tumor/weights/best.pt'
        self.mod_is_scan = 'models/is_scan/weights/best.pt'
        self.mod_is_tumor = 'models/is_tumor/weights/best.pt'


    def __get_predicted_img__(self, result_dir) -> str:
        """ Returns predicted img. """
        if not isinstance(result_dir, str):
            raise TypeError("result_dir should be a string!")
        img_path = str(result_dir) + "/"
        if os.path.exists(result_dir):
            filenames = os.listdir(result_dir)
        else:
            raise ValueError("[Wrong directory] The directory doesn't exist!")
        if len(filenames) != 1:
            wrong_file = "[Wrong directory] The directory contains more than one file. \
                          This is the predicted img directory!"
            raise ValueError(wrong_file)
        for f in filenames:
            img_path += str(f)
        return img_path


    def __preprocess_img__(self, input_image) -> None:
        """ Resize img to 640 * 640 and grayscaled the img before prediction. """
        if not isinstance(input_image, str):
            raise TypeError("[Wrong input type] The input is not a string!")
        img = cv2.imread(input_image)
        if img is None:
            raise ValueError("[Wrong image path] The inputed image is invalid!")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (640, 640), interpolation = cv2.INTER_AREA)
        cv2.imwrite("input.png", img)

    def __is_correct_filetype__(self, image):
        file_extension = os.path.splitext(image.name)[1].lower()
        if file_extension not in ['.jpg', '.jpeg', '.png', '.tiff', '.tif']:
            return False
        return True

    def __classification_model__(self, model, image):
        """Runs model, returns prediction and confidence
        1 means yes """
        # determines if image is brain scan
        use_model = YOLO(model)
        scan_results = use_model.predict(source=image, save=True)
        prediction = scan_results[0].probs.top1
        confidence = scan_results[0].probs.top1conf.item()
        return prediction, confidence

    def __segmentation_model__(self, model, image):
        locate_tumor_model = YOLO(model)
        location_results = locate_tumor_model(source=image, save=True)
        boxes = location_results[0].boxes
        if boxes.data.shape[0] == 0:
            st.write("After review, no tumor identified")
            return
        # run locate tumor model
        result_dir = location_results[0].save_dir
        img_path = self.__get_predicted_img__(result_dir)
        # st.write(img_path)
        st.image(img_path)
        st.write("Bad news, probably a tumor :(")
        return

    def render_page2(self) -> None:
        """ Renders Brain Tumor Prediction page in streamlit. """
        st_style = CustomStyle()
        st_style.config_page(page_title="Brain Tumor Prediction", page_icon="✨")
        st.markdown("<h1 style='text-align: center;'>Brain Tumor Information</h1>",
                    unsafe_allow_html=True)
        st_style.hide_header()
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

        upload_img = st.file_uploader("Choose an image")
        # ADD IN code to reject non-images
        if upload_img is not None:
            if not self.__is_correct_filetype__(upload_img):
                st.error("Please upload your file in a valid filetype. \
                         Currently accepted filetypes: .jpg, .jpeg, \
                          .png, .tiff, .tif", icon="🚨")

            # read img as bytes:
            bytes_data = upload_img.getvalue()
            bytesio_object = BytesIO(bytes_data)

            # save the img as png
            with open("input.png", "wb") as f:
                f.write(bytesio_object.getbuffer())

            # grayscale and resize to 640 * 640
            self.__preprocess_img__("input.png")

            # determines if image is brain scan
            is_scan_pred, confidence = self.__classification_model__(self.mod_is_scan, "input.png")
            if is_scan_pred == 1 and confidence > 0.95:
                is_tumor_pred, confidence = self.__classification_model__(
                    self.mod_is_tumor, "input.png")
                if is_tumor_pred == 1 and confidence > 0.95:
                    self.__segmentation_model__(self.mod_loc_t, "input.png")
                else:
                    st.write(f"Based on our current model, we believe there \
                             is no tumor found with a {confidence} level")
            else:
                st.write("Unfortunately, this image is not recognized as \
                         a brain scan. Please double-check to ensure you've \
                         uploaded a suitable brain scan image")




if __name__ == "__main__":
    page_2 = Page2()
    page_2.render_page2()

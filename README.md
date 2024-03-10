[![build_test](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml/badge.svg)](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml)
[![Coverage Status](https://coveralls.io/repos/github/tchiang0/data_515_brain_tumor_computer_vision/badge.svg?branch=main)](https://coveralls.io/github/tchiang0/data_515_brain_tumor_computer_vision?branch=main)

Brain Tumor Detection Tool Using Computer Vision Techniques
====================
As the field of deep learning continues to grow, we are interested in its application within healthcare, particularly in the realm of brain tumor detection and classification based on brain CT scans. Our project objective is to develop a user-friendly website catering to a diverse audience, including researchers, patients, doctors, and interested users in general. The platform's primary functionality involves allowing users to upload brain CT scans and receive predictions regarding the presence of a tumor and its severity. Other features of this website includes a background introduction of brain tumors, its symptoms and signs, and resources to further explore the topics.
As a stretch goal, we envision incorporating an interactive chatbot into the website. This chatbot would serve as a guide, directing users to relevant pages and, ideally, facilitating the upload of images for predictions within the chat interface. This feature not only enhances user engagement but also provides an intuitive and seamless experience for individuals seeking information or diagnostic insights.

Data Sets
====================



Folder / Structure
====================

        data_515_brain_tumor_computer_vision/
        |-README.md
        |- data_515_brain_tumor_computer_vision/
            |-ui_demo/
                |- ...
            |-model_training/
                |- ...
            |- tests/
                |- ...
        |- examples
            |-user_guide
        |- docs/
            |-Component_Specification.md
            |-DATA 515 Technology Review.pptx
            |-Function_Specification.md
            |-Milestones.md
            |-diagram.png
            |-users_usecase.md
            |-DATA 515 Technology Review.pdf
        |-pyproject.toml
        |-requirements.txt
        |-environment.yml



------------------

Software Dependencies and Installation
====================
Python 3 is required

All other dependencies are in requirments.txt file

Installation steps:

1. Clone the project repo:

        git clone https://github.com/tchiang0/data_515_brain_tumor_computer_vision.git

2. Install pip if not already installed:

        python -n pip install

3. Run requirements.txt to ensure all dependencies exist:

        pip install -r requirements.txt

--------------------
Running the tool
====================
The tool is run by opening a terminal in the data_515_brain_tumor_computer_vision folder and running the following command.

Command to run model:

    python -m streamlit run ui_demo/Brain_Tumor_Information.py

This will provide a url link that you can click to access our streamlit site in your browser.

See the user_guide.pdf in the examples folder for more information on how to use the tool.

--------------------



Use cases
====================
Doctors:

Patients:


Researchers: Adjust models ....


----------------------


Models
======================



----------------------

Appendix
====================
INCLUDE AND TEST MODEL in .py file?????
IF LEAVE OUT, JUSTIFY

Disclaimer: This tool was not created by medical professionals and is not intended to be used in place of medical practices. This is merely a tool to help researchers, patients, and doctors see how computer vision could be used for brain tumor detection and to provide resources on brain tumors.

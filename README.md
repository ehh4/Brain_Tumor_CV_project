[![build_test](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml/badge.svg)](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml)
[![Coverage Status](https://coveralls.io/repos/github/tchiang0/data_515_brain_tumor_computer_vision/badge.svg?branch=main)](https://coveralls.io/github/tchiang0/data_515_brain_tumor_computer_vision?branch=main)

Brain Tumor Detection Tool Using Computer Vision Techniques
====================
As the field of deep learning continues to grow, we were interested in its application within healthcare, particularly in the realm of brain tumor detection and classification based on brain CT scans. We developed a tool that allows researchers, patients, doctors, and interested users in general the ability to upload brain CT scans and receive predictions regarding the presence of a tumor and its severity. Other features of our tool website include a background introduction of brain tumors, its symptoms and signs, and resources to further explore the topics. Additonally, we designed a Infobot to allow users to use the website tool in an interactive manner.


Data Sets
====================
The following datasets were used for model training:

Tumor location:
https://universe.roboflow.com/mycollege/tumor-detection-2/dataset/3

Tumor vs no tumor:
https://universe.roboflow.com/mri-image-dataset/training-69oh4

Brain scans vs non brain scans: <br>
Used a subset of both of the above datasets for brain scans and used below for random images
https://www.kaggle.com/datasets/ezzzio/random-images


Folder / Structure
====================

        data_515_brain_tumor_computer_vision/
        |-README.md
        |- data_515_brain_tumor_computer_vision/
            |-model-training/
                |-sample_data/
                    |- ...
                |-model_building.py
                |-model_building_exploratory.ipynb
                |-exploratory.ipynb
            |-models/
                |-is_scan/
                    |- ...
                |-is_tumor/
                    |- ...
                |-locate_tumor/
                    |- ...
                |-locate_tumor_2/
                    |- ...
            |-tests/
                |-predict/
                    |- ...
                |-test_funcs
                |-test_streamlit
                |-test_model_building
            |-ui_demo/
                |-pages/
                    |- ...
                |-Brain_Tumor_Information
        |- examples
            |-user_guide
            |-train_models_user_guide
            |-example_brain_scans/
                |-...
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

data_515_brain_tumor_computer_vision is the main project directory which contains:

model-training: Contains a file named model_building.py with the code to build and train the models that were used. The two YOLOv8 models are for the two classification models, one to detect if an image is a brain scan, one to detect if there is a tumor or not. The .ipynb file show the training runs that we did.

models: Contains the weights and results of training for the 3 models we trained and used in the tool.

ui_demo: Contains Brain_Tumor_Information.py which is the landing page of our streamlit site. The pages directory contains the other pages for the site.

examples contains a user guide for using the tool, trainig the models, and a folder with sample brain scans for users to test the tool.

------------------

Software Dependencies and Installation
====================
Python 3 is required with conda


Installation steps:

1. Clone the project repo:

        git clone https://github.com/tchiang0/data_515_brain_tumor_computer_vision.git

2. Open a terminal and cd into the project repo:

        cd data_515_brain_tumor_computer_vision

3. Create a conda environment with the required packages with the following command:
    * Note this may take a couple minutes to install the packages <br>


            conda env create -f environment.yml

4. Activate the environment:

        conda activate project_env

5. cd into the main project directory, data_515_brain_tumor_computer_vision:

        cd data_515_brain_tumor_computer_vision

6. run the tool using:

        python -m streamlit run ui_demo/Brain_Tumor_Information.py

See user_guide in examples folder for troubleshooting and a more complete walkthough of installation

--------------------
Running the tool
====================
The tool is run by opening a terminal in the data_515_brain_tumor_computer_vision folder of the project repository and running the following command.

Command to run model:

    python -m streamlit run ui_demo/Brain_Tumor_Information.py

This will provide a url link that you can click to access our streamlit site in your browser.

See the user_guide.pdf in the examples folder for more information on how to use the tool.

--------------------



Use cases
====================
Doctors: Doctors can use the tool to get an initial review of the brain scan or use it to supplement their own review and diagnosis.

Patients: Patients can use the tool to get a prediction on their own brain scan and find resources about brain tumors.


Researchers: Researchers can use the tool to see how computer vision can be used for brain tumor detection. Additionally, they can train the models with different parameters or datasets to learn how the tool works and to improve the tool.


----------------------


Models
======================
We used the YOLOv8 base models from Ultralytics for classification and segmentation. Documentation and more information about the models can be found [here](https://docs.ultralytics.com/).



----------------------

Appendix
====================
Disclaimer: This tool was not created by medical professionals and is not intended to be used in place of medical practices. This is merely a tool to help researchers, patients, and doctors see how computer vision could be used for brain tumor detection and to provide resources on brain tumors.

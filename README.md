[![build_test](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml/badge.svg)](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml)
[![Coverage Status](https://coveralls.io/repos/github/tchiang0/data_515_brain_tumor_computer_vision/badge.svg?branch=main)](https://coveralls.io/github/tchiang0/data_515_brain_tumor_computer_vision?branch=main)

Brain Tumor Detection Tool Using Computer Vision Techniques
====================
As the field of deep learning continues to grow, we are interested in its application within healthcare, particularly in the realm of brain tumor detection and classification based on brain CT scans. Our project objective is to develop a user-friendly website catering to a diverse audience, including researchers, patients, doctors, and interested users in general. The platform's primary functionality involves allowing users to upload brain CT scans and receive predictions regarding the presence of a tumor and its severity. Other features of this website includes a background introduction of brain tumors, its symptoms and signs, and resources to further explore the topics.
As a stretch goal, we envision incorporating an interactive chatbot into the website. This chatbot would serve as a guide, directing users to relevant pages and, ideally, facilitating the upload of images for predictions within the chat interface. This feature not only enhances user engagement but also provides an intuitive and seamless experience for individuals seeking information or diagnostic insights.

Data Sets
====================



Software Dependencies
====================
Python version?

Explain how to use requirments.txt


--------------------

Folders
====================


--------------------
Running the tool
====================
The tool is run using a shell script in the data_515_brain_tumor_computer_vision folder.

Command to run model:

    python -m streamlit run ui_demo/Brain_Tumor_Information.py

This will provide a url link that can you click to access our streamlit site.


--------------------



Use case
====================







Appendix
====================
INCLUDE AND TEST MODEL in .py file?????
IF LEAVE OUT, JUSTIFY
=======
![Build/Test Workflow](https://github.com/tchiang0/data_515_brain_tumor_computer_vision/actions/workflows/build_test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/tchiang0/data_515_brain_tumor_computer_vision/badge.svg?branch=main)](https://coveralls.io/github/tchiang0/data_515_brain_tumor_computer_vision?branch=main)
### Brain Tumor Identification using Computer Vision Techniques (Instance and Sementics Segmentation)

<b>The project type:</b> Create a tool\
<b>The questions of interest:</b>\
With the brain tumor images, we want to explore computer vision methods such as instance and semantics segmentation to recognize/predict the different probability or severity of tumor presence given a brain medical image.\
<b>The goal for the project output:</b>\
An online website/tool where potential patients can upload their brain scan images and we’ll return the likelihood/severity of the brain tumor. Although that cannot serve as the ultimate truth, we can encourage patients to seek professional help.\
<b>The data sources you will use:</b>\
[Medical Image DataSet: Brain Tumor Detections](https://www.kaggle.com/datasets/pkdarabi/medical-image-dataset-brain-tumor-detection)\
[Brain Tumor Image DataSet: Instance Segmentation](https://www.kaggle.com/datasets/pkdarabi/medical-image-dataset-brain-tumor-segmentation)\
[Brain Tumor Image DataSet : Semantic Segmentation](https://www.kaggle.com/datasets/pkdarabi/brain-tumor-image-dataset-semantic-segmentation)



<b>Notes:</b>
A few related models/datasets:\
[A Complete ML Pipeline FastAI](https://www.kaggle.com/code/qitvision/a-complete-ml-pipeline-fast-ai)\
Uses fast.ai to identify cancer in scans. Example of semantics\
Fast.ai is an easy to use model that requires less parameter tuning and model customization\
Also gives an example of image augmentation using OpenCV\
Five year old example\
[Buiding a CNN Example](https://www.kaggle.com/code/fmarazzi/baseline-keras-cnn-roc-fast-10min-0-925-lb)\
Quick example using keras\
An example of building a CNN model\
Another 5 year old example
import streamlit as st
from page1 import page1
from page2 import page2
from page3 import page3
# import other functions from page1, page2, and page3

def intro():
    st.write("# Welcome to Streamlit! 👋")
    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

page1stuff = page1()
page2stuff = page2()
page3stuff = page3()

page_names_to_funcs = {
    "—": intro,
    "Brain Tumor Information": page1stuff.renderPage1,
    "Brain Tumor Prediction with Brain CT": page2stuff.renderPage2,
    "ChatBot": page3stuff.renderPage3
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
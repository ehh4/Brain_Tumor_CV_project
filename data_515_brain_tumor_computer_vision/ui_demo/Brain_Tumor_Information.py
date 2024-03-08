# pylint: disable=invalid-name
# pylint: disable=import-error
""" Brain Tumor Landing Page. """
import streamlit as st
from ui_demo.style import CustomStyle


def intro():
    """ Brain tumor background information. """
    st_style = CustomStyle()
    st_style.config_page(page_title="Brain Tumor Entry Page", page_icon="🧠")
    st_style.hide_header()
    st.markdown("<h1 style='text-align: center;'>Brain Tumor Information</h1>",
                unsafe_allow_html=True)
    st.markdown("""<p style='font-size: 20px;'>
                    An estimated 94,390 people in the U.S. will receive a primary brain tumor diagnosis in 2023. The resources below will help you throughout your experience.
                    </p>""",
                    unsafe_allow_html=True)
    st.markdown(""" ## Signs and Symptoms""")
    st.markdown("""
                #### Some of the most common signs and symptoms cause by brain tumors include but are not limited to the following:
                """)
    st.markdown("""<ul style='font-size: 20px;'>
                <li>Headache
                <li>Seizures</li>
                <li>Difficulty thinking, speaking, or finding words</li>
                <li>Changes in personality or behavior</li>
                <li>Weakness, numbness, or loss of movement in one part or one side of the body</li>
                <li>Difficulty with balance or dizziness</li>
                <li>Sensory changes like difficulty hearing, difficulty seeing, or loss of smell</li>
                <li>Memory loss</li>
                <li>Confusion in everyday matters or disorientation</li>
                <li>Unexplained nausea or vomiting</li>
                <li>Fatigue or muscle weakness</li>
                </ul>""", unsafe_allow_html=True)
    st.markdown("""<p style='font-size: 20px;'>
                    If you are diagnosed with a brain tumor, ask your provider where it is located in the brain to better prepare for possible symptoms and safety concerns.
                    </p>""",
                    unsafe_allow_html=True)
    img_path = 'ui_demo/brain_img.png'
    st.image(img_path, caption='Brain Structure and their Functions' )

    st.markdown(
      """
      ## Additional Resources

      ##### [National Brain Tumor Society](https://braintumor.org/g)
      ##### [Managing Symptoms through Palliative Care](https://shorturl.at/eoJN4)
      ##### [National Brain Tumor Society's Symptom Tracker](https://shorturl.at/p2579)
      ##### [Seattle Children’s Brain Tumor Program](https://shorturl.at/klnC4)
      """
    )

if __name__ == "__main__":
    intro()

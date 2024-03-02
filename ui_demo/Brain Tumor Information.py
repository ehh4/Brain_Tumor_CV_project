"""
Landing page: Includes brain tumor introduction (signs, symptoms, additional resources)
    intro: display the landing page.
"""
import streamlit as st
from style import st_style


def intro():
    """ Brain tumor background information. """
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


    st.image('brain_img.png', caption='Brain Structure and their Functions' )

    st.markdown(
      """
      ## Additional Resources

      ##### [National Brain Tumor Society](https://braintumor.org/g)
      ##### [Managing Symptoms through Palliative Care](https://braintumor.org/brain-tumors/diagnosis-treatment/palliative-care/)
      ##### [National Brain Tumor Society's Symptom Tracker](https://braintumor.wpenginepowered.com/wp-content/uploads/2022/04/NBTS_Symptom.Tracker_2022-fin1.pdf)
      ##### [American Society of Clinical Oncology's Cancer.Net Mobile App](https://www.cancer.net/navigating-cancer-care/managing-your-care/cancernet-mobile)
      ##### [Seattle Children’s Brain Tumor Program](https://www.seattlechildrens.org/clinics/neurosciences/services/brain-tumor-program/?utm_campaign=brain-tumor&utm_source=google&utm_medium=sem&utm_content=sponsored-search-results&utm_term=paid-search-parents-brain-tumor-program&gad_source=1&gclid=Cj0KCQiAwvKtBhDrARIsAJj-kTjf_TnnlJ2C2-Yl9jXjjbj9ucepAmZ5_ncmy0I_y4SLDlBoJ97EBPAaArbyEALw_wcB)
      """
    )


if __name__ == "__main__":
    intro()
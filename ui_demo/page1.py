import streamlit as st


class page1:
    def __init__(self) -> None:
        pass


    def renderPage1(self) -> None:
        st.write("# Brain Tumor Informations")
        st.markdown(
        """
        An estimated 94,390 people in the U.S. will receive a primary brain tumor diagnosis in 2023. The resources below will help you throughout your experience.

        ## Signs and Symptoms
        #### Some of the most common signs and symptoms cause by brain tumors include but are not limited to the following:
        - Headaches
        - Seizures 
        - Difficulty thinking, speaking, or finding words
        - Changes in personality or behavior
        - Weakness, numbness, or loss of movement in one part or one side of the body
        - Difficulty with balance or dizziness
        - Sensory changes like difficulty hearing, difficulty seeing, or loss of smell
        - Memory loss
        - Confusion in everyday matters or disorientation
        - Unexplained nausea or vomiting
        - Fatigue or muscle weakness

        If you are diagnosed with a brain tumor, ask your provider where it is located in the brain to better prepare for possible symptoms and safety concerns.
        """
        )

        st.image('brain_img.png', caption='Brain Structure and their Functions')


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
# pylint: disable=invalid-name
# pylint: disable=import-error
""" Infobot page. """
import streamlit as st
from ui_demo.style import CustomStyle


class InfobotPage:
    """ Infobot page class. """
    def __init__(self) -> None:
        pass


    # Streamed response emulator
    def response_generator(self, res_type) -> None:
        """ Generate valid bot response given valid input. """
        valid_button_vals = ["Learn about Brain Cancer", "Get Brain Tumor Prediction",
        "Get Diagnosis Next Steps", "Get Additional Help"]
        if not isinstance(res_type, str):
            raise TypeError("[Wrong response type] response should be a string")
        if res_type not in valid_button_vals:
            raise ValueError("[Wrong response]: should choose one of the valid buttons")
        learn_reponse = "To learn more about Brain Cancer, \
        you can visit our home page <br> \
        [Brain Tumor Information](http://localhost:8501/) <br> \
        or trusted outside resources such as <br> \
        [American Brain Tumor Association (ABTA)](https://www.abta.org) <br> \
        [National Brain Tumor Society](https://braintumor.org/g) \
        In case of an <b>emergency</b>, please dial <b>911</b> \
        immediately for assistance."
        help_response = "Here are some links to additional resources: <br> \
        [National Brain Tumor Society](https://braintumor.org/g) <br>\
        [Managing Symptoms through Palliative Care](https://shorturl.at/eoJN4) <br>\
        [National Brain Tumor Society's Symptom Tracker](https://shorturl.at/p2579) <br> \
        [Seattle Children’s Brain Tumor Program](https://shorturl.at/klnC4) <br> \
        In case of an <b>emergency</b>, please dial <b>911</b> \
        immediately for assistance."
        prediction_response = "Here is the \
        [Brain Tumor Prediction Page](http://localhost:8501/Brain_Tumor_Prediction)"
        diagnosis_response = "If your healthcare provider suspects a brain tumor, \
        a number of tests will be conducted, includding <br> \
        <li> A neurological exam: Test different parts of your brain to \
        understand how they are working </li> \
        <li> Head CT scan and Brain MRI\
        <li> PET scan of the brain\
        <li> Brain Biopsy: procedure to remove a sample of brain tumor tissue \
        for testing in a lab; normally conducted during brain tumor removal surgery \
        <br> A brain tumor grade, ranging from 1-4 is then assigned \
        <br> For more information, \
        please visit [Mayo Clinic](https://shorturl.at/qwA25)"
        if res_type == "Learn about Brain Cancer":
            response = learn_reponse
        elif res_type == "Get Brain Tumor Prediction":
            response = prediction_response
        elif res_type == "Get Diagnosis Next Steps":
            response = diagnosis_response
        else:
            response = help_response
        return response


    def render_infobot_page(self) -> None:
        """ Renders Infobot interface. """
        st_style = CustomStyle()
        st_style.config_page(page_title="Infobot", page_icon="🤖")
        st_style.hide_header()
        st.markdown("<h1 style='text-align: center;'>Brain Tumor Bot</h1>",
                    unsafe_allow_html=True)

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html=True)

        # # Display chat input for user to type their message
        # user_input = st.chat_input("Type your message here or choose an option below:")

        # # Check if the user has entered text and handle it
        # if user_input:
        #     st.session_state.messages.append({"role": "user", "content": user_input})
        #     with st.chat_message("user"):
        #         st.markdown(user_input, unsafe_allow_html=True)

        # Display buttons for predefined prompts
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Learn about Brain Cancer"):
                selected_prompt = "Learn about Brain Cancer"
        with col2:
            if st.button("Get Brain Tumor Prediction"):
                selected_prompt = "Get Brain Tumor Prediction"
        with col3:
            if st.button("Get Diagnosis Next Steps"):
                selected_prompt = "Get Diagnosis Next Steps"
        with col4:
            if st.button("Get Additional Help"):
                selected_prompt = "Get Additional Help"

        # Handle the selection from buttons
        if 'selected_prompt' in locals():
            response = self.response_generator(selected_prompt)

            st.session_state.messages.append({"role": "user", "content": selected_prompt})
            with st.chat_message("user"):
                st.markdown(selected_prompt, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response, unsafe_allow_html=True)


if __name__ == "__main__":
    infobot_page = InfobotPage()
    infobot_page.render_infobot_page()

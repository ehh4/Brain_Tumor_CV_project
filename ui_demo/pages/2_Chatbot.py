import streamlit as st
import random
import time
import sys
print(sys.path)

from style import st_style


class page3:
    def __init__(self) -> None:
        pass

    # Streamed response emulator
    def response_generator(self) -> None:
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    
    def renderPage3(self) -> None:
        st_style.config_page(page_title="ChatBot", page_icon="🤖")
        st_style.hide_header()
        st.title("Simple chat")

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Display chat input for user to type their message
        user_input = st.chat_input("Type your message here or choose an option below:")

        # Check if the user has entered text and handle it
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

        # Display buttons for predefined prompts
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Learn about Brain Cancer"):
                selected_prompt = "Learn about Brain Cancer"
        with col2:
            if st.button("Get Help"):
                selected_prompt = "Get Help"
        with col3:
            if st.button("Other Topics"):
                selected_prompt = "Other Topics"
        with col4:
            if st.button("Learn about my condition"):
                selected_prompt = "Learn about my condition"

        # Handle the selection from buttons
        if 'selected_prompt' in locals():
            if selected_prompt == "Learn about Brain Cancer":
                response = "To learn more about Brain Cancer, please visit the [American Brain Tumor Association (ABTA)](https://www.abta.org)."
            elif selected_prompt == "Get Help":
                response = "Here's how you can get help: [Get Help](http://example.com/gethelp)"
            elif selected_prompt == "Other Topics":
                response = "Please choose a topic."
            elif selected_prompt == "Learn about my condition":
                # Ask for tumor size and provide further information
                tumor_size = st.text_input("Please enter the size of the tumor in cm:")
                if tumor_size:
                    response = f"You entered {tumor_size} cm. [Provide next steps or information based on the tumor size]"
                else:
                    response = "Please enter the size of the tumor to proceed."

            st.session_state.messages.append({"role": "user", "content": selected_prompt})
            with st.chat_message("user"):
                st.markdown(selected_prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)


if __name__ == "__main__":  
    page_3 = page3()
    page_3.renderPage3()
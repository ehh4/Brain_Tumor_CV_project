import streamlit as st
import sys
sys.path.append('/path/to/style/directory')
from style import st_style

import random
import time
import sys
print(sys.path)

#from style import st_style


class page3:
    """
    A class to represent the third page of a Streamlit application, 
    which functions as a simple chat interface.
    """

    def __init__(self) -> None:
        """Initialize the Page3 class."""
        pass

    # Streamed response emulator
    def response_generator(self) -> str:
        """
        Generates a simulated streaming response for the chat.

        Yields:
            str: The next word in the chat response, followed by a space.
        """
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


    def handle_user_input(self, input):
        """
        Determines if the user input is non-empty.

        Parameters:
            user_input (str): The input provided by the user.

        Returns:
            bool: True if the input is non-empty, False otherwise.
        """
        if input:
            return True
        return False

    
    def renderPage3(self) -> None:
        """
        Renders the third page of the application, displaying the chat interface,
        handling user input, and responding to predefined prompts.
        """
        st_style.config_page(page_title="ChatBot", page_icon="🤖")
        st_style.hide_header()
        st.title("Chat")

        if "messages" not in st.session_state:
            st.session_state.messages = []

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
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Learn about Brain Cancer"):
                selected_prompt = "Learn about Brain Cancer"
        with col2:
            if st.button("Get Help"):
                selected_prompt = "Get Help"
        with col3:
            if st.button("Learn about my condition"):
                selected_prompt = "Learn about my condition"

        if 'selected_prompt' in locals():
            # Define response based on selected prompt
            response = self.generate_response(selected_prompt)
            st.session_state.messages.append({"role": "user", "content": selected_prompt})
            with st.chat_message("user"):
                st.markdown(selected_prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

    def generate_response(self, selected_prompt: str) -> str:
        """
        Generates a response based on the selected prompt.

        Parameters:
            selected_prompt (str): The prompt selected by the user.

        Returns:
            str: The response to the selected prompt.
        """
        if selected_prompt == "Learn about Brain Cancer":
            return "To learn more about Brain Cancer, please visit the [American Brain Tumor Association (ABTA)](https://www.abta.org)."
        elif selected_prompt == "Get Help":
            return "Here's how you can get help: [Get Help](http://example.com/gethelp)"
        elif selected_prompt == "Learn about my condition":
            tumor_size = st.text_input("Please enter the size of the tumor in cm:")
            if tumor_size:
                return f"You entered {tumor_size} cm. [Provide next steps or information based on the tumor size]"
            return "Please enter the size of the tumor to proceed."
        return "Please choose a topic."


if __name__ == "__main__":  
    page_3 = page3()
    page_3.renderPage3()
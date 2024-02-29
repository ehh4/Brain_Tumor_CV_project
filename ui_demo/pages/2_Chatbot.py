""" Interacts with user in brain tumor related information. """
import streamlit as st
import random
import time
from style import st_style


class page3:
    def __init__(self) -> None:
        pass

    # Streamed response emulator
    def response_generator(self) -> None:
        """ Chatbot generates response. """
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

    
    def render_page3(self) -> None:
        """ Renders chat interface. """
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

        # Accept user input
        if prompt := st.chat_input("What is up?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = st.write_stream(self.response_generator())
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
                

if __name__ == "__main__":  
    page_3 = page3()
    page_3.render_page3()
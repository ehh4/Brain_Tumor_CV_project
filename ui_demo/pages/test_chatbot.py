import unittest
from Chatbot import page3
#import importlib
#Chatbot = importlib.import_module("2_Chatbot").page3


class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = page3()

    def test_response_generator(self):
        response = list(self.bot.response_generator())  # Convert generator to list
        expected_responses = [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
        self.assertTrue(any(resp in expected_responses for resp in response), "The response should be one of the predefined responses")

    def test_handle_user_input(self):
        self.assertTrue(self.bot.handle_user_input("Hello"), "The method should return True for non-empty input")
        self.assertFalse(self.bot.handle_user_input(""), "The method should return False for empty input")

if __name__ == '__main__':
    unittest.main()

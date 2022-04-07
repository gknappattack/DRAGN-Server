from chatbots.Chatbot import Chatbot
import json

class Abbi(Chatbot):
    response = None

    # use this init space to initialize gpt2 for 
    def __init__(self):
        pass

    def send_message(self):
        # Save message sent from user
        msg_full = self.response['text']

        # Split and get text to feed GPT2
        text = msg_full.split(":")[1]


        print("Message sent: ", "This is Abbi")

        return {"text": "This is Abbi"}

    def recv_message(self, message):
        self.response = message


        return super().recv_message(message)
from chatbots.Chatbot import Chatbot
import json

class Trevor(Chatbot):
    response = None
    def send_message(self):
        print(self.response)
        #json_text = json.dumps(self.response)
        self.response['text'] = "Plr->4:I am Trevor Ashby"
        return self.response
    def recv_message(self, message):
        self.response = message
        return super().recv_message(message)
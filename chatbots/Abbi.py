from chatbots.Chatbot import Chatbot
from chatbots.fill_temp import fill_templates
import json

from random import randint # this is only to make the outputs a little more interesting for me when testing

class Abbi(Chatbot):
    response = None
    my_temps = ["Armageddon approaches. Only you can stop it, with the help of <person1> and <obj1>. Hurry to <location1>, and make sure <person2> does not find you, or the <group1>.", "The <obj1> of <person1> has been stolen by the <group1>. Please, you must retrieve it before the <group2> come and slaughter us in our beds.", "I require <obj1>. I expect you to bring it to me at <location1> in one day, or else <location2> in two days.", "I will smite you where you stand, you foul fiend. Draw your <obj1>, and let us commence battle here in <location1>."]

    # use this init space to initialize gpt2 for 
    def __init__(self):
        pass

    def send_message(self):
        # Save message sent from user
        msg_full = self.response['text']

        # Split and get text to feed GPT2
        text = msg_full.split(":")[1]

        resp_text = fill_templates.fill_in(self.my_temps[randint(0,len(self.my_temps)-1)])
        return {"text": msg_full.split(":")[0] + ":" + resp_text}

    def recv_message(self, message):
        self.response = message


        return super().recv_message(message)

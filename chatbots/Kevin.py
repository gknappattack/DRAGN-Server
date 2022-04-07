from chatbots.Chatbot import Chatbot
import json
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import pipeline, set_seed

class Kevin(Chatbot):
    response = None

    # use this init space to initialize gpt2 for 
    def __init__(self):
        pass

    def send_message(self):
        # Save message sent from user
        msg_full = self.response['text']

        # Split and get text to feed GPT2
        text = msg_full.split(":")[1]
    
        print(text)

        # Generate GPT2 Response
        generator = pipeline('text-generation', model='gpt2')
        set_seed(42)
        out = generator(text, max_length=30, num_return_sequences=1)
        sent_text = out[0]['generated_text']
        sent_text = "Plr->5: " + sent_text
        sent_text = sent_text.replace('\n', ' ')

        print("Message sent: ", sent_text)

        return {"text": sent_text}

    def recv_message(self, message):
        self.response = message


        return super().recv_message(message)
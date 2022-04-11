from chatbots.Chatbot import Chatbot
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import pipeline, set_seed
import gpt_2_simple as gpt2
import tensorflow as tf
import spacy
from spacy.language import Language
import random
import re



class Kevin(Chatbot):
    response = None

    # use this init space to initialize gpt2 for 
    def __init__(self):
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sess, run_name='run1', checkpoint_dir="chatbots\\checkpoint\\")
        print("Initialized GPT from checkpoint")

    ## Creating a Component is as easy as adding this decorator, and giving it a name.

    @Language.component("templater_component")
    ## passing in doc will let you have access to the document in the pipeline
    def templater_component(doc):

        for token in doc:
            #### Adds an attribute called 'is_template' ####
            
            get_is_template = lambda token: True if token.ent_type_ in ['PERSON', 'LOC', 'ORG'] else False      
            token.set_extension("is_template", getter=get_is_template, force=True)

            #### Adds an attribute called 'template_text' ####
            get_template_text = lambda token: token.ent_type_ if token.ent_type_ in ['PERSON', 'LOC', 'ORG'] else token.text    
        return doc
    

    def send_message(self):
        nlp = spacy.load("en_core_web_lg")
        nlp.add_pipe("templater_component", name="templater", last=True)

        # Genereate text from gpt2 checkpoint
        quest_msg = gpt2.generate(self.sess, run_name='run1', return_as_list=True, length=300, checkpoint_dir="chatbots\\checkpoint\\")[0]

        # Get the first quest (super jank, my gpt produced a weird string then quest stuff next)
        quest_msg = quest_msg.split('\n')[1]

        ### Testing with Adam's Spacy pipeline
        docs = nlp(quest_msg)
        print("SPACY out: ", docs)

        # Split the quest title and body text in case we want to use it.
        quest_title, quest_text = quest_msg.split(":")[0], quest_msg.split(":")[1]

        # Temporary to make sure it fits.
        quest_msg = "5->Plr: " + quest_msg[:150]
        quest_msg += "..."

        '''
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
        '''

        print("Message sent: ", quest_msg)

        return {"text": quest_msg}

    def recv_message(self, message):
        self.response = message


        return super().recv_message(message)
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:53:02 2016

@author: Valentin
"""
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1#
import os

def say_text(text):
    text_to_speech = TextToSpeechV1(
        username="bd5e5bb7-0e46-4e74-9224-39cbbae10acf",
        password="1ahwxmR1XE5x",
        x_watson_learning_opt_out=True)  # Optional flag

    # print(json.dumps(text_to_speech.voices(), indent=2))



    # print(os.getcwd().replace('\\','/'))

    with open(os.getcwd().replace('\\','/')+'/currentSpeech.wav', 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(text, accept='audio/wav', voice="de-DE_BirgitVoice"))

    os.system("start "+os.getcwd().replace('\\','/')+'/currentSpeech.wav')
# print(json.dumps(text_to_speech.pronunciation('Watson', pronunciation_format='spr'), indent=2))
#
# print(json.dumps(text_to_speech.customizations(), indent=2))

# print(json.dumps(text_to_speech.create_customization('test-customization'), indent=2))

# print(text_to_speech.update_customization('YOUR CUSTOMIZATION ID', name='new name'))

# print(json.dumps(text_to_speech.get_customization('YOUR CUSTOMIZATION ID'), indent=2))

# print(json.dumps(text_to_speech.get_customization_words('YOUR CUSTOMIZATION ID'), indent=2))

# print(text_to_speech.add_customization_words('YOUR CUSTOMIZATION ID',
#                                              [{'word': 'resume', 'translation': 'rɛzʊmeɪ'}]))

# print(text_to_speech.set_customization_word('YOUR CUSTOMIZATION ID', word='resume',
#                                             translation='rɛzʊmeɪ'))

# print(json.dumps(text_to_speech.get_customization_word('YOUR CUSTOMIZATION ID', 'resume'), indent=2))

# print(text_to_speech.delete_customization_word('YOUR CUSTOMIZATION ID', 'resume'))

# print(text_to_speech.delete_customization('YOUR CUSTOMIZATION ID'))

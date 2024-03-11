import streamlit as st
import os
import time
import glob
import os


from gtts import gTTS
from googletrans import Translator

translator = Translator()

def get_audio(theText="Sorry, no input"):
    tld = "com"
    tts = gTTS(theText, lang="en", tld=tld, slow=False)

    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio_okay"
    tts.save(f"{my_file_name}.mp3")
    return my_file_name

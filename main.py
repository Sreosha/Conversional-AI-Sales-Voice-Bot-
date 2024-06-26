from transcribe_voice import *
from receive_voice import *
from response import *

import sounddevice as sd
from scipy.io.wavfile import write
import openai
import wavio as wv
from openai import OpenAI
import os
from dotenv import load_dotenv
import time
from elevenlabs.client import ElevenLabs
from elevenlabs import stream, play



load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLAB_KEY =  os.getenv('ELEVENLAB_KEY')

if __name__ == "__main__":
    voice_path = "audio/recording_temp.wav"
    generate_voice(voice_path)
    transcribed_audio_text = transcribe_audio(voice_path)
    llm_response = get_ai_response(str(transcribed_audio_text))
    tts(llm_response)
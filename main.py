'''
@Author: Senkita
'''

from speech_recognition import SpeechRecognition
from utils import *
from setting import audio_path

def main():
    sr = SpeechRecognition(
        audio_path
    )
    
    log(sr.speech_recognition())

if __name__ == "__main__":
    main()
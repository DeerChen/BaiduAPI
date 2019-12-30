'''
@Author: Senkita
'''

from api.speech_recognition import SpeechRecognition
from lib.utils import *
from lib.setting import AUDIO_PATH

def main():
    sr = SpeechRecognition(
        AUDIO_PATH
    )
    
    log(sr.speech_recognition())

if __name__ == "__main__":
    main()
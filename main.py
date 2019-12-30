'''
@Author: Senkita
'''

from api.speech_recognition import SpeechRecognition
from api.speech_synthesis import SpeechSynthesis
from lib.utils import *
from lib.setting import AUDIO_PATH

def main():
    sr = SpeechRecognition(
        AUDIO_PATH
    )
    text = sr.speech_recognition()[0]
    ss = SpeechSynthesis(
        text
    )
    ss.speech_synthesis()

if __name__ == "__main__":
    main()
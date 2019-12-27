'''
@Author: Senkita
'''

from speech_recognition import SpeechRecognition
from utils import *

def main():
    client_id = 'appKey'
    client_secret = 'secretKey'
    audio_path = '文件位置'

    sr = SpeechRecognition(
        client_id,
        client_secret,
        audio_path
    )
    log(sr.speech_recognition())

if __name__ == "__main__":
    main()
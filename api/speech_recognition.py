'''
@Author: Senkita
'''

import time
import json
import os
import base64
import requests
from .base import Base
from .parent_dir import *
from lib.utils import *
from lib.setting import CUID

# 语音识别
class SpeechRecognition(Base):
    def __init__(self, audio_path):
        super().__init__()
        self.audio_path = audio_path
        self.access_token_dict = None
        self.speech, self.len = self.audio_base64()
        self.api_url = "https://vop.baidu.com/server_api"
    
    # 验权
    def verification(self):
        while (self.access_token_dict is None) or (self.access_token_dict['deadline'] <= time.time()):
            self.access_token_dict = self.authentication()
        assert ('audio_voice_assistant_get' in self.access_token_dict['scope']), Error('请到百度智能云平台增授语音识别权限')
        return self.access_token_dict['access_token']

    # 获取音频大小并编码
    def audio_base64(self):
        try:
            file_size = os.path.getsize(self.audio_path)
            with open(self.audio_path, 'rb') as f:
                speech = base64.b64encode(f.read()).decode('utf-8')
                return (speech, file_size)
        except:
            raise Error('文件未找到')
    
    # 组装json
    def assemble_data_json(self):
        data = {
            'format': 'pcm',
            'rate': 16000,
            'channel': 1,
            'cuid': CUID,
            'token': self.verification(),
            'dev_id': 1537,
            'speech': self.speech,
            'len': self.len
        }
        return json.dumps(data)

    # 语音识别
    def speech_recognition(self):
        headers = {
            'Content-Type': 'application/json'
        }
        result_response = requests.post(
            url = self.api_url,
            data = self.assemble_data_json(),
            headers = headers
        )
        result = result_response.json().get('result')
        return result
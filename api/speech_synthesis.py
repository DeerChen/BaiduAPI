'''
@Author: Senkita
'''

import time
import requests
from urllib.parse import urlencode
from .base import Base
from .parent_dir import *
from lib.utils import *
from lib.setting import CUID

# 语音合成
class SpeechSynthesis(Base):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.access_token_dict = None
        self.api_url = "https://tsn.baidu.com/text2audio"
    
    # 验权
    def verification(self):
        while (self.access_token_dict is None) or (self.access_token_dict['deadline'] <= time.time()):
            self.access_token_dict = self.authentication()
        assert ('public' in self.access_token_dict['scope']), Error('请到百度智能云平台增授语音合成权限')
        return self.access_token_dict['access_token']

    # 文本编码
    def text_urlencode(self):
        assert (len(self.text) <= 2048), Error('文本过长')
        text_dict = dict(
            tex = self.text
        )
        return urlencode(text_dict)[4:]
    
    # 组装params
    def assemble_params(self):
        params = {
            'tex': self.text_urlencode(),
            'tok': self.verification(),
            'cuid': CUID,
            'ctp': 1,
            'lan': 'zh',
            'spd': 5,
            'pit': 5,
            'vol': 5,
            'per': 111,
            'aue': 6
        }
        return urlencode(params)

    # 语音合成
    def speech_synthesis(self):
        result_response = requests.post(
            url = self.api_url,
            data = self.assemble_params(),
        )
        result = result_response.headers.__getitem__('Content-Type')
        assert (result == 'audio/wav'), Error('语音合成失败')
        with open('demo.wav', 'wb') as f:
            f.write(result_response.content)
        return result
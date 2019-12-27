'''
@Author: Senkita
'''

import requests
import time
from utils import *

# api共用基础类
class Base:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = 'client_credentials'
        self.authorization_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type={}&client_id={}&client_secret={}'.format(
            self.grant_type,
            self.client_id,
            self.client_secret
        )

    # 鉴权
    def authentication(self):
        try:
            response = requests.post(
                self.authorization_url
            )
            if response:
                response_json = response.json()
                shelf_life = response_json.get('expires_in')
                access_token_dict = {
                    'access_token': response_json.get('access_token'),
                    'deadline': time.time() + shelf_life,
                    'scope': response_json.get('scope')
                }
                return access_token_dict
        except:
            raise Error('请求出错，请检查网络或请求参数')
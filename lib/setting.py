'''
@Author: Senkita
'''

import uuid
import hashlib

# appKey
CLIENT_ID = ''
# secretKey
CLIENT_SECRET = ''
# pcm音频文件位置
AUDIO_PATH = ''
# MAC地址md5加密做cuid
CUID = hashlib.md5(
    uuid.UUID(
        int=uuid.getnode()
    ).hex[-12:].encode()
).hexdigest()
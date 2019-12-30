'''
@Author: Senkita
'''

import uuid
import hashlib

# appKey
client_id = ''
# secretKey
client_secret = ''
# pcm音频文件位置
audio_path = ''
# MAC地址md5加密做cuid
cuid = hashlib.md5(
    uuid.UUID(
        int=uuid.getnode()
    ).hex[-12:].encode()
).hexdigest()
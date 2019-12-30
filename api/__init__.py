'''
@Author: Senkita
'''

import os
import sys

# 将上级目录加入环境变量
sys.path.append(
    os.path.abspath(
        os.path.dirname(__file__) + os.sep + '../'
    )
)
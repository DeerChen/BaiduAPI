'''
@Author: Senkita
'''

import time

# 封装print方法
def log(*kwargs, **args):
    record_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(record_time, *kwargs, **args)

# 自定义异常类
class Error(Exception):
    def __init__(self, error):
        self.error = error
    def __str__(self):
        return repr(self.error)
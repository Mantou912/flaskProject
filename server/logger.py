import os
import time


class Logger:
    def __init__(self, path='./source/') -> None:
        self.__path = path
        if not os.path.exists(self.__path):
            print('创建log路径...')
            os.makedirs(self.__path)

    def log(self, data) -> None:
        """把数据存入log文件中"""
        filename = ''
        for each in time.localtime()[: 3]: filename += f'_{each}'
        filename += '.txt'

        with open(self.__path + filename, 'a', encoding='utf-8') as f:
            f.write(str(time.localtime()[: 6]) + data + '\n')

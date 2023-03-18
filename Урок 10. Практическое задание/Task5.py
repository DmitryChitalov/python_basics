"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

arg1 = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(arg1, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    source_encoding_ya = chardet.detect(line)
    line = line.decode(source_encoding_ya['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

arg2 = ['ping', 'youtube.com']
YOU_PING = subprocess.Popen(arg2, stdout=subprocess.PIPE)
for line in YOU_PING.stdout:
    source_encoding_you = chardet.detect(line)
    line = line.decode(source_encoding_you['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

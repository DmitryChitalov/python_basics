"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!

"""

import subprocess
import chardet

yandex = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for elem in yandex:
    yandex_ping = subprocess.Popen(elem, stdout=subprocess.PIPE)
    for line in yandex_ping.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))

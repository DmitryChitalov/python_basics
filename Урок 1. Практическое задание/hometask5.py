# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

# Подсказки:
# --- используйте модуль chardet, иначе задание не засчитается!!!

import urllib.request, chardet

yan = urllib.request.urlopen('http://yandex.ru/').read()
print(chardet.detect(yan))
try:
    print(yan.decode(chardet.detect(yan)['encoding']))
except:
    print('Кодировка не известна')
you = urllib.request.urlopen('https://www.youtube.com/').read()
print(chardet.detect(you))
try:
    print(you.decode(chardet.detect(you)['encoding']))
except:
    print('Кодировка не известна')
# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

# Подсказки:
# --- используйте списки и циклы, не дублируйте функции


list_1 = ['разработка','администрирование','protocol','standard']
for i in list_1:
    enc = i.encode('utf-8')
    print(enc, type(enc))
    dec = bytes.decode(enc, 'utf-8')
    print(dec, type(dec))
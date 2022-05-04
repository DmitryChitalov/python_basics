"""
Из методички не понял как делать. Сделал по этому мануалу:
https://programka.com.ua/rukovodstvo/klaster/kak-najti-naibolshuju-cifru-v-chisle-v-python
"""
number = int(input('Введите целое число: '))
print(max(map(int, [_ for _ in str(number)])))

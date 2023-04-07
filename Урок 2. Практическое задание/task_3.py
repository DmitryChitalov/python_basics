
mseason = {'Зима': [12, 1, 2],'Весна': [3, 4, 5],'Лето': [6, 7, 8],'Осень': [9, 10, 11]}
month = int(input('Введите мясяц 1-12: '))
result = ''
for season in mseason:
  if month in mseason[season]:
      result = season.capitalize()
      break
  else:
      result = 'Не правильно указали месяц'
print(result)


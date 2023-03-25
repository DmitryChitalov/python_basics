# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input())
ticket1 = ticket // 100000
ticket2 = ticket // 10000
ticket22 = ticket2 % 10
ticket3 = ticket // 1000
ticket33 = ticket3 % 10
ticket4 = ticket // 100
ticket44 = ticket4 % 10
ticket5 = ticket // 10
ticket55 = ticket5 % 10
ticket6 = ticket % 10
ticketFirstThreeNumbers = ticket1 + ticket22 + ticket33
ticketLastThreeNumbers = ticket44 + ticket55 + ticket6
if ticketFirstThreeNumbers == ticketLastThreeNumbers:
    print('yes')
else:
    print('no')
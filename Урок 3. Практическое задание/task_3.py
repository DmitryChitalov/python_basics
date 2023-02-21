"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func_first(arg_1, arg_2, arg_3):
    sequence_numbers = [arg_1, arg_2, arg_3]
    sequence_numbers.sort()
    print(sequence_numbers[1] + sequence_numbers[2])    
my_func_first(10, 5, 20)

def my_func_second(arg_1, arg_2, arg_3):
    sequence_numbers = [arg_1, arg_2, arg_3]
    print(sum(sequence_numbers) - min(sequence_numbers))   
my_func_second(10, 5, 20)
    
    
    
    

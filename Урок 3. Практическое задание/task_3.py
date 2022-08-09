"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(a,b,c):
    user_input = [a,b,c]
    user_input.sort(reverse=True)
    return(user_input[0]+user_input[1])


def my_func_no_sort(a,b,c):
    user_input = [a,b,c]

    largest = max(user_input)
    user_input.remove(largest)
    second_largest = max(user_input)

    return largest + second_largest


first_number, second_number, third_number  = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter third number : "))

print(my_func(first_number, second_number, third_number))

print(my_func_no_sort(first_number, second_number, third_number))
"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def summ_numbers(user_data: str, special_character: str):
    """
    Prompts for an array of numbers, separated by space and calculates their sum until user enters a special character.
    :param user_data: String of numbers, separated by space
    :param special_character: Special character used to break the function execution
    :return: Integer - sum of numbers passed in user_data argument

    """
    result = 0
    user_data = user_data.split(" ")  # Convert string to a list

    for i in user_data:
        if i != special_character:  # Check if user entered special character
            try:
                result += float(i)  # Add number to the result
            except ValueError:
                print(
                    f"{i} is not a number. Skipping..."
                )  # Ignore if user entered data is not integer
        else:
            break  # Exit, if user entered a speial character
    return result


user_data = ""
special_character = input("Please provide a character you want to use as breaker : ")
summ = 0

while special_character not in user_data:
    user_data = input("Please enter numbers:")
    summ += summ_numbers(user_data, special_character)
    print(summ)

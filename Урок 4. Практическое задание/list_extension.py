import string_extension

def get__int_numbers_from_list(input_list):
    number_list =[]
    for el in input_list:
        if string_extension.is_int(el):
            number_list.append(int(el))
    return number_list
def my_sum():
    arg_1 = str(input('Put Your Name: '))
    arg_2 = str(input('Put Your Surname: '))
    arg_3 = str(input('Put Your DOB: '))
    arg_4 = str(input('Put Your City: '))
    arg_5 = str(input('Put Your Email: '))
    arg_6 = str(input('Put Your Phone number: '))
    return list[f'Name: {arg_1}; Surname: {arg_2}; DOB: {arg_3}; City: {arg_4}; Email: {arg_5}; Phone number: {arg_6};']


print(my_sum())

def division(a, b):
    try:
        c = a / b
        return c
    except:
        return 'Incorrect data'



a = int(input('Input "a": '))
b = int(input('Input "b": '))
result = division(a, b)

print('Result:', result)
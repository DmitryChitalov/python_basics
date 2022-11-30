def int_func(text):
    text = text.split()
    result = []
    for el in range(len(text)):
        buffer = text[el]
        buffer2 = buffer[0]
        buffer2 = buffer2.upper()
        result.append(buffer2 + buffer[1:len(buffer)])
    return " ".join(result)

def int_func1(text):
    return text.title()


print(int_func(input("Введите текст: ")))
print(int_func1(input("Введите текст: ")))
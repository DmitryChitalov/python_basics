def int_func(text):
    buffer = text[0]
    buffer = buffer.upper()
    text = buffer + text[1:len(text)]
    return text

def int_func1(text):
    return text.title()


print(int_func(input("Введите текст: ")))
print(int_func1(input("Введите текст: ")))
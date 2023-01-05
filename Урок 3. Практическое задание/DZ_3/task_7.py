# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

print("Введите текст")
my_text = input(" > ")


def edit(text):
    arg = str.__str__(text)
    res = arg.title()
    return res


res = edit(my_text)
print(res)
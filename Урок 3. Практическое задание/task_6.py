def int_func(word):
    return word.capitalize()


input_str = input("Введите строку из слов: ")
words = input_str.split()
capitalized_words = [int_func(word) for word in words]
output_str = " ".join(capitalized_words)

print(output_str)

print("Введите текст:\n")
text = []
while True:
    buffer = input()
    if len(buffer) > 0:
        text.append(buffer + "\n")
    else:
        break
out_f = open("out_file.txt", "w", encoding='utf-8')
out_f.writelines(text)
out_f.close()
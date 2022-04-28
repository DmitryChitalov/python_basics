file_open = open('1.txt', 'w')
while True:
    text_line = str(input("Input text line: \n"))
    if text_line == "print":
        file_open = open('1.txt', 'r')
        print("\nPrint file:\n----------\n" + file_open.read() + "---------- \nEnd file.")
        break
    elif not text_line:
        print("Exit.\n")
        break
    elif text_line:
        file_open.write(text_line + "\n")
file_open.close()
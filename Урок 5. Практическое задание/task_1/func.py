def write_file(file_path, line):
    """
    Функция записывает строку текста в файл
    :param file_path: путь до файла
    :param line: строка текста
    :return:

    Пример вызова: write_file("my_file.txt", "text to file ...")
    """
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(line)
    except IOError as e:
        print(f"IOError: {e}")

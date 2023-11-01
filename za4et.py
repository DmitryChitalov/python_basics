import os
import argparse
import logging

def group_rename_files(directory, desired_name, num_digits, src_extension, dest_extension, name_range=(0, -1)):
    # Получаем список файлов в указанной директории с заданным расширением
    files = [f for f in os.listdir(directory) if f.endswith(src_extension)]

    # Проверяем, что диапазон сохраняемого оригинального имени в пределах длины имени файла
    if name_range[0] < 0 or name_range[1] >= len(files[0]):
        logging.error("Неверный диапазон для сохраняемого оригинального имени")
        return

    # Переменная для отслеживания порядкового номера
    counter = 1

    for filename in files:
        # Извлекаем часть имени файла в соответствии с заданным диапазоном
        original_name = filename[name_range[0]:name_range[1] + 1]

        # Создаем новое имя файла, добавляя желаемое имя, порядковый номер и расширение
        new_filename = f"{desired_name}{original_name}{counter:0{num_digits}d}{dest_extension}"

        # Собираем полные пути к исходному и новому файлам
        src_path = os.path.join(directory, filename)
        dest_path = os.path.join(directory, new_filename)

        try:
            # Переименовываем файл
            os.rename(src_path, dest_path)
            logging.info(f"Переименован файл: {filename} -> {new_filename}")
        except Exception as e:
            logging.error(f"Ошибка при переименовании файла {filename}: {str(e)}")

        counter += 1

def main():
    parser = argparse.ArgumentParser(description="Групповое переименование файлов")
    parser.add_argument("directory", help="Директория, в которой находятся файлы")
    parser.add_argument("desired_name", help="Желаемое конечное имя файлов")
    parser.add_argument("num_digits", type=int, help="Количество цифр в порядковом номере")
    parser.add_argument("src_extension", help="Расширение исходного файла")
    parser.add_argument("dest_extension", help="Расширение конечного файла")
    parser.add_argument("--name_range", type=int, nargs=2, default=[0, -1], help="Диапазон сохраняемого оригинального имени (по умолчанию, 0 - до конца)")
    args = parser.parse_args()

    logging.basicConfig(filename='rename_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    group_rename_files(args.directory, args.desired_name, args.num_digits, args.src_extension, args.dest_extension, args.name_range)

if __name__ == "__main__":
    main()

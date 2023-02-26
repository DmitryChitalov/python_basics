"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

if __name__ == '__main__':
    try:
        with open('text', 'r') as f_obj:
            s = 0
            for i in f_obj:
                s += 1
                print(f"{s} строка содержит {len(i.split())} слов")
    except IOError:
        print('Warning: error input output')
    except Exception as e:
        print(e)


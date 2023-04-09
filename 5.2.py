with open('task02.txt') as f:
    rows = f.readlines()
    expanded_rows = [row.split() for row in rows]

rows_count, words_count = len(rows), sum([len(word_list) for word_list in expanded_rows])

print(f"Всего строк - {rows_count}, всего слов - {words_count}")
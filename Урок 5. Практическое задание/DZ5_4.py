trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
trans_obj = open("DZ5_4.txt", 'r', encoding='utf-8')
new_trans_obj = open("DZ5_4_new.txt", 'w', encoding='utf-8')
for line in trans_obj:
    for word in line.split(' '):
        if word in trans_dict.keys():
            new_trans_obj.write(trans_dict[word] + ' ')
        else:
            new_trans_obj.write(word + ' ')
trans_obj.close()
new_trans_obj.close()

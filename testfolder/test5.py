
with open('newinfo.txt', 'w', encoding='utf-8') as object_file:
    print('Love you baby - ', file=object_file)




"""outfile = open('info2.txt', 'w', encoding='utf-8')
added_lines = ['string_1\n','string_2\n', 'string_3\n']
outfile.writelines(added_lines)
outfile.close()
print()"""

"""outfile = open('info2.txt', 'w', encoding='utf-8')
outfile.write('NewText Added !!')
outfile.close()"""


"""
my_info = open('info.txt', 'r', encoding='utf-8')
for el in my_info:
    print(el)
my_info.close()"""


"""my_info = open('info.txt', 'r', encoding='utf-8')
read_cont = my_info.readlines()
print(read_cont)
my_info.close()

"""

"""new_info = open('newinfo.txt', 'w', encoding='utf-8')
read_count2 = new_info.read()
print(read_count2)
new_info.close()"""

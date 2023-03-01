edu_list = open('DZ5_6.txt', 'r', encoding='UTF-8')
edu_dict = {}
edu_sum = 0
num_list = []
num = 0
for line in edu_list:
    edu_tmp = line.split(':')
    num_list.clear()
    for char in edu_tmp[1]:
        if char.isdigit():
            num += char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    edu_sum = sum(num_list)
    tmp_dict = {edu_tmp[0] : edu_sum}
    edu_dict.update(tmp_dict)
print(edu_dict)
edu_list.close()
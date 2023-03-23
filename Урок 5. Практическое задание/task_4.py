with open('task4_1.txt', 'r') as input_file:
    with open('task4_2.txt', 'w') as output_file:
        for line in input_file:
            line = line.replace('One', 'Один')
            line = line.replace('Two', 'Два')
            line = line.replace('Three', 'Три')
            line = line.replace('Four', 'Четыре')
            output_file.write(line)

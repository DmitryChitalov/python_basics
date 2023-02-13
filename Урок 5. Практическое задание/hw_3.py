first_f = open("file_3.txt", "r", encoding='utf-8')
lines = first_f.readlines()
first_f.close()
total = 0
count = 0
for line in lines:
    surname, salary = line.split()
    count += 1
    total += int(salary)
    if int(salary) < 20000:
        print(f"Surname: {surname} salary: {salary}")
print (f"Average salary: {total/count}")
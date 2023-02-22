from sys import argv

production = argv[1]
rate = argv[2]
prize = argv[3]
def my_salary(production, rate, prize):
    return (production * rate) + prize

print(my_salary(float(argv[1]), int(argv[2]), int(argv[3])))

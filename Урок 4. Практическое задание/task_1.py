import sys


def calculate_salary(hours, rate, bonus):
    salary = hours * rate + bonus
    return salary


if __name__ == '__main__':
    try:
        hours = float(sys.argv[1])
        rate = float(sys.argv[2])
        bonus = float(sys.argv[3])
    except IndexError:
        print("Usage: Петров <hours> <rate> <bonus>")
        sys.exit(1)
    except ValueError:
        print("Error: invalid input")
        sys.exit(1)

    salary = calculate_salary(hours, rate, bonus)
    print(f"Salary: {salary}")
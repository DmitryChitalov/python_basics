from sys import argv
script_name, hours, hour_rate, premium = argv
payment = (int(hours) * int(hour_rate)) + int(premium)
print(f"Размер заработной платы = {payment}")
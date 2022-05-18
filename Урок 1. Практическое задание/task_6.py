start = int(input("input a: "))
finish = int(input("input b: "))
day = 1
print(f"{day} day: {start}")
while start < finish:
    start += start * 0.1
    day += 1
    print(f"{day} day: {start:.2f}")
print(f"Answer: on the {day} day, the athlete achieved a result of at least {finish}km.")

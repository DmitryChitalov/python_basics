proceeds = int(input("input proceeds: "))
costs = int(input("input costs: "))
if proceeds > costs:
    profit = proceeds - costs
    print(f"financial result: profit! its value: {profit}")
    print(f"profitability of proceeds: {profit / proceeds}")
    people = int(input("input number of people working in the company: "))
    print(f"the company's profit per person: {profit / people}")
else:
    print(f"financial result: losses! its value: {costs - proceeds}")

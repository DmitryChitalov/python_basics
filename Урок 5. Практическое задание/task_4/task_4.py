input_dict = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
with open("text4.txt", "r", encoding='1251') as f:
    for el in f:
        for el2 in input_dict.keys():
            el = el.replace(el2, input_dict[el2])
        print(el)
        with open("newfile4.txt", "a") as f2:
            f2.write(f"\n {el}")

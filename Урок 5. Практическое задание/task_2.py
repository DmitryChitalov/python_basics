with open("2_task.txt", "r", encoding="utf-8") as f_obj:
    lines = 0
    words = 0
    n = 0
    for line in f_obj:
        lines += line.count("\n")
        n += 1
        words = len(line.split(" "))
        print(f"Words in {n} line- {words}")
    print(f"lines in text- {lines}")


"""
Words in 1 line- 8
Words in 2 line- 9
Words in 3 line- 8
lines in text- 3  
"""

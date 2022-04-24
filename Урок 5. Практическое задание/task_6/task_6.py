final_dict = {}
with open("text6.txt", "r", encoding='1251') as f:
    for line in f:
        clear_line = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(".", "")
        subject, lec, prac, lab = clear_line.split()

        lect = 0
        practice_ = 0
        lab = 0
        if lec != "-":
            lect = int(lec)
        if prac != "-":
            practice = int(prac)
        if lab != "-":
            lab = int(lab)
        final_dict[subject] = lect + practice + lab
    print(final_dict)

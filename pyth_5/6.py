with open(r"C:\Users\Катя\Desktop\text_6.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()

    # мне кажется, эти два абзаца с тремя переменными можно записать короче, но я не знаю как ))
        lecture = lecture[0:-3]
        practice = practice[0:-4]
        lab = lab[0:-5]

        lecture = 0 if lecture == '' else lecture
        practice = 0 if practice == '' else practice
        lab = 0 if lab == '' else lab

        print(f'Суммарные часы предмета "{subject}" = {int(lecture) + int(practice) + int(lab)}')

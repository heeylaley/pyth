with open(r"C:\Users\Катя\Desktop\text_3.txt", encoding='utf-8') as f_obj:
    sum_int = 0
    n = 0
    for line in f_obj:
        n += 1  # считаю строчки так, потому что если написать len(f_obj.readlines) то with выполняет только эту
        # операцию и игнорирует всё остальное
        spl = line.split()
        print(spl[0], f'з/п = {spl[1]} тыс.') if int(spl[1]) <= 20 else False
        sum_int += int(spl[1])
    print(sum_int / n)

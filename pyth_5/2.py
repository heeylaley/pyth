f_obj = open(r"C:\Users\Катя\Desktop\text_2.txt")

content = f_obj.readlines()
print(f'Количество строк в файле = {len(content)}')

n = 0
for el in content:
    n += 1
    print(f'Строка {n}: количество элементов = {len(el.split())}')

f_obj.close()

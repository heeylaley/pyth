list_1 = [300, 67, 9, 76, 11, 17, 0, 8, 99, 99, 7]

list_2 = [el for el in list_1 if el > list_1[list_1.index(el) - 1]]
# есть две проблемы: 1) с таким способом включает 300 (тк 300 > 7) и 2) два раза пишет 99
# я понимаю почему это происхоит но не знаю как написать чтоб это исправить
print(list_2)
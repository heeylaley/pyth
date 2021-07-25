inp_str = str(input("Введите элементы списка через запятую с пробелом: "))
inp_list = list(inp_str.split(', '))

a = 0
while a < len(inp_list) - 1:
    inp_list[a], inp_list[a + 1] = inp_list[a + 1], inp_list[a]
    a += 2
print(inp_list)

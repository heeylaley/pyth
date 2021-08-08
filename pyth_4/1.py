from sys import argv

script_name, w_time, wages, bonus = argv

count = (int(w_time) * int(wages)) + int(bonus)
print(f'Ваша заработная плата = {count}')

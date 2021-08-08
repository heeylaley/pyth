pre_list = [1, 2, 2, 67, 88, 88, 4, 67, 10, 11, 2, 10]

end_list = [el for el in pre_list if pre_list.count(el) == 1]
print(end_list)

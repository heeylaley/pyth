my_str = input("Введите предложение: ")

words = list(my_str.split())

for el in words:
    print(words.index(el) + 1, el.title()[0: 11])

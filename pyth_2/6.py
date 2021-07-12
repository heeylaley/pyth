dict_1 = {"название": " ", "цена": " ", "количество": " ", "ед. измерения": " "}
dict_2 = dict_1.copy()
dict_3 = dict_1.copy()


def dict_input(a, b):
    a["название"] = input(f"{b}. Введите название товара: ")
    a["цена"] = input("Введите цену товара: ")
    a["количество"] = input("Введите количество товара (в ед. измерения): ")
    a["ед. измерения"] = input("Введите единицы измерения: ")
    return a


while dict_3 == dict_1:
    dict_input(dict_1, b=1)
    dict_input(dict_2, b=2)
    dict_input(dict_3, b=3)

list_goods = [
                tuple([1, dict_1]),
                tuple([2, dict_2]),
                tuple([3, dict_3])
             ]

print("Изначальный список товаров:")
for el in list_goods:
    print(el)

print("Аналитика товаров:")

val_1 = [dict_1["название"], dict_2["название"], dict_3["название"]]
val_2 = [dict_1["цена"], dict_2["цена"], dict_3["цена"]]
val_3 = [dict_1["количество"], dict_2["количество"], dict_3["количество"]]
val_4 = [dict_1["ед. измерения"], dict_2["ед. измерения"], dict_3["ед. измерения"]]

dict_4 = {"названия": list(set(val_1)),
          "цена": list(set(val_2)),
          "количество": list(set(val_3)),
          "единицы": list(set(val_4))}

print(dict_4)

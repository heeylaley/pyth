def data_base():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    date_of_birth = input("Введите дату вашего рождения (чч.мм.гг): ")
    place_of_liv = input("Введите место вашего проживания: ")
    email = input("Введите ваш email: ")
    phone_num = input("Введите ваш номер телефона: ")
    return (f"Имя и фамилия: {name} {surname}, Дата рождения: {date_of_birth}, Место рождения: {place_of_liv}, "
            f"email: {email}, Номер телефона: {phone_num}")


print(data_base())

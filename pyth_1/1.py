name = input("Давай знакомиться! Как тебя зовут?: ")

print(f"Рад познакомиться, {name}.")

age = int(input("А теперь скажи мне свой возраст: "))

if 5 >= age > 0 or age >= 100:
    print("Так я и поверил")
    print("Попробуй ещё раз")
    quit()
elif age < 0:
    print("Отрицательный возраст - это что-то новенькое!")
    print("Попробуй ещё раз")
    quit()
else:
    print("Ну что ж, будем знакомы! До скорого! :^)")

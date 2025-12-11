numbers = [10, 20, 30, 40, 50]
print("Исходный список:", numbers)

try:
    divisor = float(input("Введите делитель: "))

    print("\nРезультаты деления:")
    for num in numbers:
        try:
            result = num / divisor
            print(f"{num} / {divisor} = {result:.2f}")  # :.2f - округление до 2 знаков после запятой
        except ZeroDivisionError:
            print(f"{num} / {divisor} = Ошибка: деление на ноль!")

except ValueError:
    print("Ошибка! Пожалуйста, введите число.")
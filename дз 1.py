
print("=== ПРОГРАММА ДЛЯ ВЫЧИСЛЕНИЯ СУММЫ ЧИСЕЛ ===")

numbers = []

for i in range(5):
    while True:
        try:
            value = float(input(f"Введите число {i+1}: "))
            numbers.append(value)
            break
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

print(f"\nВаш список чисел: {numbers}")
print(f"Сумма всех чисел: {sum(numbers)}")
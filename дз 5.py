animals = ["Собака", "Кошка", "Попугай", "Хомяк", "Рыбка"]
print("Наш список животных:", animals)

user_input = input("\nВведите название животного для удаления: ").strip()

try:
    if not user_input:
        print("Вы ничего не ввели!")
    else:
        animals.remove(user_input)
        print(f"✓ Животное '{user_input}' успешно удалено!")
        print("Обновленный список:", animals)

except ValueError:
    print(f"✗ Животное '{user_input}' не найдено в списке.")

    print("Доступные животные в списке:")
    for animal in animals:
        print(f"  - {animal}")

except KeyboardInterrupt:
    print("\nПрограмма прервана.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
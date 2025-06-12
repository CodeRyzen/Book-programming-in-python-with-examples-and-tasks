def second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("Список должен содержать как минимум два элемента")
    
    unique_numbers = list(set(numbers))  # Убираем повторы
    if len(unique_numbers) < 2:
        raise ValueError("Недостаточно уникальных значений для поиска второго по величине числа")
    
    unique_numbers.sort(reverse=True)  # Сортировка по убыванию
    return unique_numbers[1]  # Второе по величине

# Пример использования:
nums = [10, 5, 8, 10, 3]
result = second_largest(nums)
print("Второе по величине число:", result)

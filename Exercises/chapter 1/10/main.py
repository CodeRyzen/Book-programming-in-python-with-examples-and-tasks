def sum_odd_numbers(count):
    sum_result = 0
    number = 1  # первое нечетное число
    for _ in range(count):
        sum_result += number
        number += 2  # следующее нечетное число
    return sum_result

# Пример использования:
print(sum_odd_numbers(5))  # Выведет 25 (1 + 3 + 5 + 7 + 9)

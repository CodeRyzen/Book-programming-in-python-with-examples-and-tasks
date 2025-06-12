def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введите число: "))

if number < 0:
    print("Ошибка: Введено отрицательное число. Введите положительное число.")
else:
    result = factorial(number)
    print(f"Факториал числа {number} равен {result}")

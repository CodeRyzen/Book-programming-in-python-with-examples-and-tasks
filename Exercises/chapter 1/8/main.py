def fibonacci_sequence(count):
    a, b = 1, 1
    for _ in range(count):
        print(a)
        a, b = b, a + b

n = int(input("Количество выведенных чисел: "))
fibonacci_sequence(n)

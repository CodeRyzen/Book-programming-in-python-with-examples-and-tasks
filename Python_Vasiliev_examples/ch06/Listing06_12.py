num=10
# Функция на основе лямбда-выражения:
L=lambda n: 2*n+1
# Проверка результата:
print("Нечетные числа:")
for k in range(num):
    print(L(k),end=" ")
# Новое значение:
L=lambda n: 2**n
# Проверка результата:
print("\nСтепени двойки:")
for k in range(num):
    print(L(k),end=" ")
# Прямой вызов лямбда-функции:
print("\nКвадраты чисел:")
for k in range(num):
    print((lambda x: x*x)(k+1),end=" ")
# Обычная функция:
def calc(x,y):
    return x+y
# Использование функции в лямбда-выражении:
F=lambda x,y: calc(x,y)
# Переменной присваивается имя функции:
f=calc
# Имени функции присваивается лямбда-выражение:
calc=lambda x,y: x*y
# Проверка результата:
print("\nВызов F(3,5):",F(3,5))
print("Вызов f(3,5):",f(3,5))
print("Вызов calc(3,5):",calc(3,5))

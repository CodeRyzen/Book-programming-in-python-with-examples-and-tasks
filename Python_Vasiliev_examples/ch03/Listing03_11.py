# Подключение функций для генерирования случайных чисел:
from random import *
# Инициализация генератора случайных чисел:
seed(2019)
# Создание списка из случайных чисел:
A=[randint(10,20) for k in range(15)]
# Содержимое списка:
print("A:",A)
# Подсчет элементов с разными значениями:
for a in range(min(A),max(A)+1):
    print(a,"-",A.count(a))
# Наибольшее, наименьшее и среднее значения:
print("Наименьший:")
print("A[",A.index(min(A)),"]=",min(A),sep="")
print("Наибольший:")
print("A[",A.index(max(A)),"]=",max(A),sep="")
print("Среднее:",sum(A)/len(A))
# Сортировка списка:
B=sorted(A)
A.sort(reverse=True)
# Проверка содержимого списков:
print("A:",A)
print("B:",B)

# Импорт функций для генерирования случайных чисел:
from random import *
# Функция для отображения вложенного списка:
def show(A):
    for a in A:
        for s in a:
            print(s,end=" ")
        print()
# Функция для создания вложенного списка
# из случайных чисел:
def rands(m,n):
    res=[[randint(0,9) for i in range(n)] for j in range(m)]
    return res
# Функция для создания вложенного списка из букв:
def symbs(m,n):
    val='A'
    res=[['' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
           res[i][j]=val
           val=chr(ord(val)+1)
    return res
# Создание вложенного списка:
A=[[(j+1)*10+i+1 for i in range(5)] for j in range(3)]
print("Список A:")
# Отображение вложенного списка:
show(A)
# Инициализация генератора случайных чисел:
seed(2019)
# Список случайных чисел:
B=rands(3,4)
print("Список B:")
# Отображение вложенного списка:
show(B)
# Список с буквами:
C=symbs(3,5)
print("Список C:")
# Отображение вложенного списка:
show(C)
# Список определяет количество строк во вложенном списке:
size=[3,5,4,6]
# Создание вложенного списка:
D=[['*' for k in range(s)] for s in size]
print("Список D:")
# Отображение вложенного списка:
show(D)

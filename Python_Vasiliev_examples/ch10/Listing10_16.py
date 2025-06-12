from threading import Thread
from time import sleep
# Функции для выполнения в дочерних потоках:
def from_left():
    global first,last,L
    val=10
    while True:
        if first<last:
            L[first]=val
            val+=10
            first+=1
            sleep(0.3)
        else:
            break
def from_right():
    global first,last,L
    val="A"
    while True:
        if first<last:
            L[last]=val
            val=chr(ord(val)+1)
            last-=1
            sleep(0.3)
        else:
            break
# Размер списка:
size=11
# Создание списка:
L=["*" for k in range(size)]
# Начальный и конечный индексы:
first=0
last=len(L)-1
print("Список до заполнения:")
print(L)
# Создание объектов дочерних потоков:
A=Thread(target=from_left)
B=Thread(target=from_right)
# Запуск потоков на выполнение:
A.start()
B.start()
# Ожидание завершения потоков:
A.join()
B.join()
# Результат заполнения списка:
print("Список после заполнения:")
print(L)


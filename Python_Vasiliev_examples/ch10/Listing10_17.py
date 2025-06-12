from threading import *
from time import sleep
# Функция для вычисления суммы:
def mysum(n,N):
    res=0
    for k in range(N+1):
        res+=k**n
        sleep(0.1)
    return res
# Функция для выполнения в дочернем потоке:
def display(n,N):
    # Блокировка объекта блокировки:
    mylock.acquire()
    # Получение ссылки на текущий поток:
    t=current_thread()
    # Отображение имени потока:
    print("Поток:",t.name)
    print("Слагаемых:",N)
    print("Степень:",n)
    # Результат вычислений:
    print("Сумма:",mysum(n,N))
    print("-------------")
    # Разблокирование объекта блокировки:
    mylock.release()
# Создание объекта блокировки:
mylock=Lock()
# Список с названиями потоков:
names=["Alpha","Bravo","Charlie","Delta"]
# Создание списка с объектами потоков:
T=[Thread(target=display,args=[k+1,10],name=names[k]) for k in range(len(names))]
# Запуск потоков на выполнение:
for t in T:
    t.start()
# Ожидание завершения выполнения потоков:
for t in T:
    t.join()

    

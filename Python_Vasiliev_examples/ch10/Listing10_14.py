from threading import *
from time import sleep
# Функция для выполнения в потоке:
def display(txt):
    A=[1,2]
    B=["A","B"]
    sleep(1)
    # Ожидание установки флага:
    myevent.wait()
    # Отмена установки флага:
    myevent.clear()
    for a in A:
        print("[",a,"] ",txt,sep="")
    # Установка флага:
    myevent.set()
    sleep(1)
    # Ожидание установки флага:
    myevent.wait()
    # Отмена установки флага:
    myevent.clear()
    for b in B:
        print("[",b,"] ",txt,sep="")
    # Установка флага:
    myevent.set()
# Создание объекта:
myevent=Event()
# Установка флага:
myevent.set()
# Объекты дочерних потоков:
F=Thread(target=display,args=["Первый"])
S=Thread(target=display,args=["Второй"])
# Запуск дочерних потоков:
F.start()
S.start()
# Ожидание завершения дочерних потоков:
F.join()
S.join()

    
    
    

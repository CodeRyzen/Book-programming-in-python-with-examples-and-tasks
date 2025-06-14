from threading import *
from time import sleep
# Функция для вызова в потоке:
def mysum():
    # Глобальная переменная:
    global num
    # Добавка к сумме:
    k=1
    # Текст для отображения:
    txt=str(num)
    # Вычисление суммы:
    while myevent.is_set():
        # К сумме прибавляется слагаемое:
        num+=k
        # Новое значение для текста:
        txt+=" + "+str(k)
        # Отображение текущего значения суммы:
        print("[",k,"] ",txt," = ",num,sep="")
        # Добавка для следующей итерации:
        k+=1
        # Пауза в выполнении потока:
        sleep(0.3)
print("Сумма целых чисел")
# Создание объекта дочернего потока:
t=Thread(target=mysum)
# Начальное значение для суммы:
num=0
# Объект для синхронизации потоков:
myevent=Event()
# Установка флага:
myevent.set()
# Запуск дочернего потока на выполнение:
t.start()
# Пауза в выполнении главного потока:
sleep(2)
# Отмена флага:
myevent.clear()
# Ожидание завершения выполнения дочернего потока:
if t.is_alive():
    t.join()
# Результат вычислений:
print("Результат:",num)


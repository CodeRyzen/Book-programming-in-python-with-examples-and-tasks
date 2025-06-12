# Класс исключения:
class MyError(Exception):
    # Конструктор:
    def __init__(self):
        self.values=[]
    # Метод обрабатывает операцию сложения:
    def __add__(self,val):
        self.values.append(val)
        return self
# Функция с рекурсивным вызовом генерирует исключение:
def getMyError(n):
    # Контролируемый код:
    try:
        if n<=1:
            # Генерирование исключения:
            raise MyError
        # Рекурсивный вызов функции:
        getMyError(n-1)
    # Обработка исключения:
    except MyError as error:
        # Генерирование исключения:
        raise error+n
# Функция для создания списка:
def getList(n):
    # Контролируемый код:
    try:
        # Вызов функции, генерирующей исключение:
        getMyError(n)
    # Обработка исключения:
    except MyError as error:
        # Результат функции:
        return error.values
# Создание списков:
A=getList(10)
print(A)
B=getList(7.5)
print(B)


# Класс исключения:
class MyError(Exception):
    # Конструктор:
    def __init__(self,code=0,msg="Исключение MyError"):
        self.code=code
        self.message=msg
    # Метод для приведения к текстовому формату:
    def __str__(self):
        txt=self.message+"\nКод ошибки: "+str(self.code)
        return txt
# Внешний блок контролируемого кода:
try:
    print("Создаем собственную ошибку")
    # Внутренний блок контролируемого кода:
    try:
        # Генерирование исключения:
        raise MyError(123)
    # Внутренний блок обработки исключения:
    except MyError as error:
        print(error)
        # Изменение параметров объекта ошибки:
        error.code=321
        error.message="Та же ошибка MyError"
        # Повторное генерирование исключения:
        raise
# Вешний блок обработки исключения:
except Exception as error:
    print(error)

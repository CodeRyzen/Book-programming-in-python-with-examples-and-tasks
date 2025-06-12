# Функция результатом получает ссылку на класс
# и результатом возвращает ссылку на класс:
def F(Alpha):
    # Внутренний класс:
    class Bravo:
        value=Alpha()
    Bravo.__name__="My"+Alpha.__name__
    return Bravo
# Описание класса:
class Charlie:
    # Конструктор:
    def __init__(self):
        self.number=123
    # Метод для отображения значения поля:
    def show(self):
        print("Поле number:",self.number)
# Создание объекта на основе класса,
# полученного при вызове функции:
obj=F(Charlie)()
# Проверка результата:
obj.value.show()
print("Класс объекта obj:",obj.__class__.__name__)
print("Класс поля value:",obj.value.__class__.__name__)

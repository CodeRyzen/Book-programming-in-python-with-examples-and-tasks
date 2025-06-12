# Первый класс:
class Alpha:
    # Поле класса:
    code=123
    # Конструктор:
    def __init__(self,num):
        print("Конструктор №1")
        self.number=num
        print("Создан объект")
        self.show()
    # Метод:
    def show(self):
        print("Метод №1")
        print("Класс:",self.__class__.__name__)
        print("Код класса:",self.__class__.code)
        print("Поле number:",self.number)
# Второй класс:
class Bravo(Alpha):
    # Поле класса:
    code=456
# Третий класс:
class Charlie(Bravo):
    # Конструктор:
    def __init__(self,num,txt):
        print("Конструктор №2")
        self.number=num
        self.name=txt
        print("Новый объект")
        self.show()
    # Переопределение метода:
    def show(self):
        print("Метод №2")
        print("Класс:",self.__class__.__name__)
        print("Код класса:",self.__class__.code)
        print("Поле number:",self.number)
        print("Поле name:",self.name)
# Четвертый класс:
class Delta(Charlie):
    # Поле класса:
    code=789
# Создание объекта:
A=Alpha(100)
# Создание поля объекта:
A.code=321
print("После команды A.code=321")
# Вызов метода:
A.show()
# Создание объектов:
B=Bravo(200)
C=Charlie(300,"C")
D=Delta(400,"D")

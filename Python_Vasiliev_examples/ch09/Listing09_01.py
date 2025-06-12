# Базовый класс:
class Alpha:
    # Конструктор:
    def __init__(self):
        self.set(100)
        print("Объект класса Alpha:",self.number)
    # Методы:
    def set(self,n):
        self.number=n
    def show(self):
        print(self.__class__.__name__,self.number)
# Производный класс:
class Bravo(Alpha):
    # Конструктор:
    def __init__(self):
        self.set(200)
        print("Объект класса Bravo:",self.number)
# Объект базового класса:
A=Alpha()
A.set(123)
A.show()
# Объект производного класса:
B=Bravo()
B.set(321)
B.show()


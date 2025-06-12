# Базовый класс:
class Alpha:
    # Методы:
    def display(self):
        print("Метод из Alpha")
        print("Поле code:",self.code)
    def show(self):
        self.display()
# Производный класс:        
class Bravo(Alpha):
    # Переопределение метода:
    def display(self):
        print("Метод из Bravo")
        print("Поле name:",self.name)
# Создание объектов:        
A=Alpha()
A.code=123
B=Bravo()
B.name="B"
# Вызов методов:
A.show()
B.show()

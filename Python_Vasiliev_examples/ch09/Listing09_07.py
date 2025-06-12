# Первый класс:
class Alpha:
    # Конструктор:
    def __init__(self,num):
        self.code=num
        print("Присвоено значение полю code")
    # Метод:
    def show(self):
        print("Поле code:",self.code)
# Второй класс:
class Bravo(Alpha):
    # Конструктор:
    def __init__(self,num,txt):
        # Вызов конструктора базового класса:
        super().__init__(num)
        self.name=txt
        print("Присвоено значение полю name")
    # Метод:
    def show(self):
        # Вызов метода из базового класса:
        super().show()
        print("Поле name:",self.name)
# Третий класс:
class Charlie(Bravo):
    # Конструктор:
    def __init__(self,num,txt,val):
        # Вызов конструктора базового класса:
        super().__init__(num,txt)
        self.value=val
        print("Присвоено значение полю value")
    # Метод:
    def show(self):
        # Вызов метода из базового класса:
        super().show()
        print("Поле value:",self.value)
# Создание объектов и вызов методов:
print("Объект A")
A=Alpha(100)
A.show()
print("Объект B")
B=Bravo(200,"B")
B.show()
print("Объект C")
C=Charlie(300,"C",[1,2,3])
C.show()

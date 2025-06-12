# Первый класс:
class Alpha:
    # Конструктор:
    def __init__(self,num):
        self.code=num
    # Метод:
    def show(self):
        print("Класс Alpha:",self.code)
# Второй класс:
class Bravo(Alpha):
    # Переопределение метода:
    def show(self):
        print("Класс Bravo:",self.code)
        super().show()
# Третий класс:
class Charlie(Alpha):
    # Переопределение метода:
    def show(self):
        print("Класс Charlie:",self.code)
        super(Charlie,self).show()
# Четвертый класс:
class Delta(Bravo,Charlie):
    # Переопределение метода:
    def show(self):
        print("Класс Delta:",self.code)
        super().show()
        Charlie.show(self)
        super(Bravo,self).show()
# Функция для отображения цепочки наследования:
def display(MyClass):
    print("Наследование для "+MyClass.__name__+":")
    k=1
    for s in MyClass.__mro__:
        print("["+str(k)+"]",s.__name__)
        k+=1
# Отображение цепочек наследования,
# создание объектов и вызов метода:
display(Alpha)
A=Alpha(100)
A.show()
display(Bravo)
B=Bravo(200)
B.show()
display(Charlie)
C=Charlie(300)
C.show()
display(Delta)
D=Delta(400)
D.show()

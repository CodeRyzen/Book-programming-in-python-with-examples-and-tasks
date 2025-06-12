# Первый класс:
class Alpha:
    code=123
    def alpha(self):
        print("Alpha:",self.code)
# Второй класс:
class Bravo(Alpha):
    def bravo(self):
        print("Bravo:",self.code)
# Третий класс:
class Charlie(Bravo):
    def charlie(self):
        print("Charlie:",self.code)
# Функция для отображения иерархии наследования:
def show(MyClass):
    print("Класс",MyClass.__name__,end=":\n")
    for s in MyClass.__mro__:
        print("<",s.__name__,">",end="",sep="")
    print()
# Иерархия наследования классов:
show(Alpha)
show(Bravo)
show(Charlie)
# Создание объектов:
A=Alpha()
B=Bravo()
C=Charlie()
# Вызов методов:
print("Объект A")
A.alpha()
print("Объект B")
B.alpha()
B.bravo()
print("Объект C")
C.alpha()
C.bravo()
C.charlie()
# Присваивание значения полю:
Bravo.code=321
print("Выполнена команда Bravo.code=321")
# Вызов методов:
print("Объект C")
C.alpha()
C.bravo()
C.charlie()
print("Объект A")
A.alpha()

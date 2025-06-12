# Первый базовый класс:
class Alpha:
    def alpha(self):
        print("Класс Alpha")
# Второй базовый класс:
class Bravo:
    def bravo(self):
        print("Класс Bravo")
# Третий базовый класс:
class Charlie:
    def charlie(self):
        print("Класс Charlie")
# Производный класс:
class Delta(Alpha,Bravo,Charlie):
    pass
# Иерархия наследования:
print("Наследование:")
k=1
for s in Delta.__mro__:
    print("["+str(k)+"]",s.__name__)
    k+=1
# Объект производного класса:
obj=Delta()
# Вызов методов:
obj.alpha()
obj.bravo()
obj.charlie()

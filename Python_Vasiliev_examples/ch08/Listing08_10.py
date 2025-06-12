# Первый класс:
class Alpha:
    "Это класс Alpha"
    pass
# Второй класс:
class Bravo:
    "Это класс Bravo"
    pass
# Информация о классах:
print(Alpha.__doc__)
print(Bravo.__doc__)
# Объекты классов:
A=Alpha()
B=Bravo()
# Изменение строки документирования:
Alpha.__doc__="Первый класс"
B.__class__.__doc__="Второй класс"
# Информация о классах:
print(A.__class__.__doc__)
print(B.__doc__)

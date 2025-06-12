# Первый класс:
class Alpha:
    pass
# Второй класс:
class Bravo:
    pass
# Переменной присваивается имя класса:
MyClass=Alpha
# Создание объекта:
A=MyClass()
# Переменной присваивается имя класса:
MyClass=Bravo
# Создание объекта:
B=MyClass()
# Присваивание классов:
Alpha=Bravo
# Создание объекта:
C=Alpha()
# Получение ссылки на объект реализации класса:
MyClass=A.__class__
# Создание объекта:
D=MyClass()
# Проверка типа объектов:
print("Объект A:",type(A).__name__)
print("Объект B:",type(B).__name__)
print("Объект C:",type(C).__name__)
print("Объект D:",type(D).__name__)
# Изменение названия классов:
MyClass.__name__="First"
Bravo.__name__="Second"
# Проверка типа объектов:
print("Объект A:",type(A).__name__)
print("Объект B:",type(B).__name__)
print("Объект C:",type(C).__name__)
print("Объект D:",type(D).__name__)

# Описание класса:
class MyClass:
    # Поле класса:
    color="Красный"
    # Методы класса:
    def set(txt):
        MyClass.color=txt
    def show():
        print(MyClass.color)
# Вызов методов класса:
MyClass.show()
MyClass.set("Зеленый")
# Отображение значения поля класса:
print(MyClass.color)
# Новое значение для поля класса:
MyClass.color="Синий"
# Вызов метода класса:
MyClass.show()
# Создание объектов класса:
A=MyClass()
B=MyClass()
# Проверка значения поля:
print("Класс:",MyClass.color)
print("Объект A:",A.color)
print("Объект B:",B.color)
# Присваивание значения полю:
A.color="Белый"
# Проверка значения поля:
print("Класс:",MyClass.color)
print("Объект A:",A.color)
print("Объект B:",B.color)
# Присваивание значения полю:
MyClass.color="Желтый"
# Проверка значения поля:
print("Класс:",MyClass.color)
print("Объект A:",A.color)
print("Объект B:",B.color)
# Удаление поля из объекта A:
del A.color
# Проверка значения поля:
print("Класс:",MyClass.color)
print("Объект A:",A.color)
print("Объект B:",B.color)




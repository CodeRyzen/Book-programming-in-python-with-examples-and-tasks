# Описание класса:
class MyClass:
    # Конструктор:
    def __init__(self):
        self.value=123
        print("Создается объект:",self.value)
    # Деструктор:
    def __del__(self):
        print("Удаляется объект:",self.value)
    # Метод для присваивания значения полю:
    def set(self,n):
        self.value=n
    # Метод для отображения значения поля:
    def show(self):
        print("Поле объекта:",self.value)
# Создание объекта:
obj=MyClass()
# Вызов методов из объекта:
obj.show()
obj.set(100)
# Вызов методов из класса:
MyClass.show(obj)
MyClass.set(obj,200)
# Проверка значения поля:
obj.show()
# Явный вызов конструктора:
MyClass.__init__(obj)
# Явный вызов деструктора:
MyClass.__del__(obj)
# Проверка значения поля:
obj.show()
# Изменение значения поля:
obj.value=321
obj.show()
# Явный вызов конструктора через объект:
obj.__init__()
# Явный вызов деструктора через объект:
obj.__del__()
# Проверка значения поля:
obj.show()

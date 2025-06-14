# Класс со специальными методами:
class MyClass:
    # Конструктор:
    def __init__(self,val):
        self.value=val
    # Метод для приведения к текстовому типу:
    def __str__(self):
        return "Поле "+str(self.value)
    # Метод для приведения к логическому типу:
    def __bool__(self):
        if type(self.value)==int:
            return True
        else:
           return False
    # Метод для приведения к целочисленному типу:
    def __int__(self):
        if self:
            return self.value
        else:
            return 0
# Создание объектов и проверка методов:
print("Объект A:")
A=MyClass(100)
print(A)
print("Число",int(A))
print("A - 1 =",int(A)-1)
print("Объект B:")
B=MyClass("B")
print(B)
print("Число",int(B))
print("B + 1 =",int(B)+1)

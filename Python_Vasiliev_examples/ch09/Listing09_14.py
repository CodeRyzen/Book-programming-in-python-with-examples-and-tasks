# Класс со специальным методом:
class Alpha:
    # Метод вызывается если атрибута нет:
    def __getattr__(self,name):
        return len(name)
# Класс со специальным методом:
class Bravo:
    # Обычный метод:
    def show(self,x):
        print("Метод show():",x)
    # Метод вызывается если атрибута нет:
    def __getattr__(self,name):
        if len(name)<5:
            return lambda x: print("Первый метод:",x)
        else:
            return lambda x: print("Второй метод:",x*x)
# Создание объектов и обращение к атрибутам:
print("Объект A класса Alpha")
A=Alpha()
A.value="Alpha"
print("Поле value:",A.value)
print("Поле color:",A.color)
print("Поле myattribute:",A.myattribute)
print("Объект B класса Bravo")
B=Bravo()
B.show(10)
B.hi(10)
B.display(10)


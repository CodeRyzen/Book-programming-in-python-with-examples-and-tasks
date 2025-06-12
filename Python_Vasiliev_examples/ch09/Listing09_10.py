# Класс со специальными методами:
class MyClass:
    # Конструктор:
    def __init__(self,num):
        self.code=num
    # Метод для преобразования к текстовому формату:
    def __str__(self):
        return str(self.code)
    # Метод для перегрузки оператора сложения:
    def __add__(self,n):
        if type(n)==int:
            val=self.code+n
        else:
            val=0
        return MyClass(val)
# Создание объекта и проверка методов:
A=MyClass(100)
print("Объект A:",A)
# К объекту прибавляется число:
B=A+25
print("Объект B:",B)
# К объекту прибавляется текст:
C=A+"Hello"
print("Объект C:",C)

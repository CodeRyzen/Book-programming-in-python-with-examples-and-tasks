# Класс со специальными методами:
class Alpha:
    # Метод для получения доступа к атрибуту:
    def __getattribute__(self,name):
        print("Alpha: запрос поля",name)
        return object.__getattribute__(self,name)
    # Метод вызывается если атрибута нет:
    def __getattr__(self,name):
        print("Нет такого поля!")
        return "Alpha: "+name
# Класс со специальным методом:
class Bravo:
    # Метод для получения доступа к атрибуту:
    def __getattribute__(self,name):
        print("Bravo: запрос поля",name)
        try:
            res=object.__getattribute__(self,name)
        except AttributeError:
            res="Bravo: нет поля "+name
        return res
# Создание объектов и обращение к полям:
print("Объект A класса Alpha")
A=Alpha()
A.value=123
print("Поле value:",A.value)
print("Еще раз:",object.__getattribute__(A,"value"))
A.value=321
print("Поле value:",A.value)
print(A.color)
print("Объект B класса Bravo")
B=Bravo()
B.mylist=[1,2,3]
print("Поле mylist:",B.mylist)
print("Еще раз:",object.__getattribute__(B,"mylist"))
B.mylist=["A","B","C"]
print("Поле mylist:",B.mylist)
print(B.myset)


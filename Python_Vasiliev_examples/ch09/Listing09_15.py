# Класс со специальным методом:
class Alpha:
    # Метод для присваивания значения атрибуту:
    def __setattr__(self,name,val):
        if name=="number" and type(val)!=int:
            res=0
        else:
            res=val
        self.__dict__[name]=res
# Создание объекта:
A=Alpha()
# Операции с полями объекта:
A.value="Объект A"
print("A.value =",A.value)
A.number=123
print("A.number =",A.number)
A.number="Hello"
print("A.number =",A.number)
A.value=321
print("A.value =",A.value)
A.__dict__["number"]="Python"
print("A.number =",A.number)


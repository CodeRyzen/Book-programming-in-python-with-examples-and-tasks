# Класс со специальными методами:
class Alpha:
    # Метод вызывается если атрибута нет:
    def __getattr__(self,name):
        return "такого атрибута нет"
    # Метод вызывается при удалении атрибута:
    def __delattr__(self,name):
        if name=="number":
            print("Удалять нельзя!")
        else:
            object.__delattr__(self,name)
# Создание объекта:
A=Alpha()
# Операции с полями объекта:
A.value="объект A"
print("value:",A.value)
del A.value
print("value:",A.value)
A.number=123
print("number:",A.number)
del A.number
print("number:",A.number)
del A.__dict__["number"]
print("number:",A.number)

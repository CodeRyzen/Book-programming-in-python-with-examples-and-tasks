# Описание класса:
class MyClass:
    # Конструктор:
    def __init__(self,val):
        # Если аргумент целочисленный:
        if type(val)==int:
            self.number=val
        # Если аргумент текстовый:
        elif type(val)==str:
            self.name=val
        # Если аргумент - действительное число:
        elif type(val)==float:
            self.value=val
        # Прочие случаи:
        else:
            self.data=val
    # Метод для отображения значения поля:
    def show(self):
        # Список с названиями полей:
        L=["number","name","value","data"]
        # Перебор названий полей:
        for s in L:
            # Если поле существует:
            if s in dir(self):
                # Отображение названия и значения поля:
                print(s,"=",self.__dict__[s])
                # Завершение оператора цикла:
                break
        # Если поле не найдено:
        else:
            print("Странный объект")
# Создание объектов и проверка полей:
A=MyClass(123)
A.show()
del A.number
A.show()
B=MyClass("Объект B")
B.show()
C=MyClass(2.5)
C.show()
D=MyClass([1,2,3])
D.show()

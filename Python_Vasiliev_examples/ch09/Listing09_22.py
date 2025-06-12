# Класс итератора:
class MyClass:
    # Конструктор:
    def __init__(self,*vals):
        L=[]
        for v in vals:
           if type(v)==int:
               if v<10 and v>0:
                   L.append(v)
        self.digits=L
        self.position=-1
    # Метод вызывается при вызове функции iter():
    def __iter__(self):
        return self
    # Метод вызывается при вызове функции next():
    def __next__(self):
        self.position+=1
        if self.position<len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration
# Создание итератора:
A=MyClass(2,"A",12,7,-3,"Hello",9,5,"Alpha")
# Вызов функции next():
try:
    while True:
        print(next(A),end=" ")
except StopIteration:
    print()
# Создание итератора:
B=MyClass(5,"B",1.2,11,-1,"Hi",8,4,"Bravo",3)
# Оператор цикла:
for s in B:
    print(s,end=" ")
print()

# Первый класс:
class Alpha:
    # Конструктор:
    def __init__(self,*vals):
        L=[]
        for v in vals:
           if type(v)==int:
               L.append(v)
        self.nums=L
    # Метод вызывается при вызове функции iter():
    def __iter__(self):
        return Bravo(self.nums)
# Второй класс:
class Bravo:
    # Конструктор:
    def __init__(self,nums):
        L=[]
        for n in nums:
            if n<10 and n>0:
                L.append(n)
        self.digits=L
        self.position=-1
    # Метод вызывается при вызове функции next():
    def __next__(self):
        self.position+=1
        if self.position<len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration
# Создание объекта класса Alpha:
A=Alpha(2,"A",12,7,-3,"Hello",9,5,"Alpha")
# Создание объекта класса Bravo:
B=iter(A)
# Вызов функции next():
try:
    while True:
        print(next(B),end=" ")
except StopIteration:
    print()
    

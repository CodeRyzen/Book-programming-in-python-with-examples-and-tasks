# Класс с перегрузкой операторов:
class Alpha:
    # Конструктор:
    def __init__(self,lst):
        self.vals=[]
        if type(lst)==list:
            for n in lst:
               self.vals.append(n)
    # Метод для приведения к текстовому формату:
    def __str__(self):
        return str(self.vals)
    # Унарный оператор "плюс":
    def __pos__(self):
        x=self.vals[0]
        del self.vals[0]
        self.vals.append(x)
        return self
    # Унарный оператор "минус":
    def __neg__(self):
        x=self.vals[-1]
        del self.vals[-1]
        self.vals.insert(0,x)
        return self
    # Умножение объекта на операнд:
    def __mul__(self,v):
        self.vals.append(v)
        return self
    # Умножение операнда на объект:
    def __rmul__(self,v):
        self.vals.insert(0,v)
        return self
    # Сокращенная форма операции умножения:
    def __imul__(self,v):
        return self*v
# Создание объекта:
A=Alpha([1,"A",2])
# Выполнение операций с объектом:
print(A)
print(+A)
print(-A)
print(A*3)
print(4*A)
A*="Alpha"
print(A)

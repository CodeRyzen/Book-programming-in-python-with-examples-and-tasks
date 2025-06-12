# Класс для вычислений чисел Фибоначчи:
class Fibs:
    # Метод вызывается при индексировании объекта:
    def __getitem__(self,n):
        a=1
        b=1
        for k in range(n-2):
            a,b=b,a+b
        return b
# Создание объекта:
F=Fibs()
# Вычисление чисел Фибоначчи:
for k in range(1,16):
    print(F[k],end=" ")
print()
 

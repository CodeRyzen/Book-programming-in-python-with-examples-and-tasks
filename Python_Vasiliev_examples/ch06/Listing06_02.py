# Импорт функций для генерирования случайных чисел:
from random import *
# Функция для отображения содержимого списков,
# множеств, текста и словарей:
def show(L,symb):
   for s in L:
      print(symb,s,sep="",end="")
   print(symb)
# Исходные данные:
A=[1,2,3,4,5]         # Список
B={'A','B','C','D'}   # Множество
C="Python"            # Текст
D={"A":1,"B":2,"C":3} # Словарь
# Вызов функции:
show(A,"|")
show(B,"/")
show(C,"*")
show(D,"#")
# Функция для создания списка чисел:
def get_nums(n,state):
    if type(n)!=int:
       return []
    if state:
        L=list(2*(k+1) for k in range(n))
    else:
        L=list(2*k+1 for k in range(n))
    return L
# Вызов функции:
print(get_nums(10,True))
print(get_nums(8,False))
print(get_nums(12.5,True))
# Функция для создания множества случайных букв:
def get_symbs(n):
    if n>10 or n<1:
       num=10
    else:
       num=n
    S=set()
    Nmin=ord("A")
    Nmax=ord("Z")
    while len(S)<num:
       S.add(chr(randint(Nmin,Nmax)))
    return S
# Инициализация генератора случайных чисел:
seed(2019)
# Вызов функции:
print(get_symbs(7))
print(get_symbs(-5))
print(get_symbs(15))

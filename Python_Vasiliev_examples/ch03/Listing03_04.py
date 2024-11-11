# Кортеж чисел:
A=tuple(k for k in range(1,21) if k%3!=0)
print(A)
# Список чисел:
B=[2**(k//2) if k%2==0 else 3**(k//2) for k in range(15)]
print(B)
# Список чисел:
C=[0 if k==0 or k==1 else k**2 for k in range(13) if not k in [2,5,7]]
print(C)
# Кортеж в обратном порядке:
Alpha=A[::-1]
print(Alpha)
# Элементы выбираются "через один", начиная с первого:
Bravo=B[::2]
print(Bravo)
# Элементы выбираются "через один", начиная со второго:
Charlie=B[1::2]
print(Charlie)

from fractions import Fraction
from decimal import Decimal
print("Дробные значения:")
A=Fraction(2,5)
print("A =",A)
B=Fraction(3,7)
print("B =",B)
C=A+B
print("A+B =",C)
print("Действительные числа:")
X=2/5
print("X =",X)
D=X+B
print("X+B =",D)
print("Числа заданной точности:")
A=Decimal('1.01')
print("A =",A)
B=Decimal('2.02')
print("B =",B)
C=A+B
print("A+B =",C)
print("1.01+2.02 =",1.01+2.02)


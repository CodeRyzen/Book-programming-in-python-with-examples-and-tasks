# Считывание верхней границы суммы:
n=int(input("Number: "))
# Начальное значение для суммы:
s=0
# Начальное значение индексной переменной:
k=0
# Оператор цикла для вычисления суммы:
while k<n:
    # Увеличение значения индексной переменной на единицу:
    k=k+1
    # Прибавление слагаемого к сумме:
    s=s+k
# Отображение результата:
print("The sum of the numbers from 1 to ",n," is ",s)

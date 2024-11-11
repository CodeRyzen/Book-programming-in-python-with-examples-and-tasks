# Вводится выражение:
val=eval(input("Введите выражение: "))
# Используется тернарный оператор:
a,b=(val[0],val[-1]) if type(val)==str else (val,type(val))
# Значения переменных:
print(a)
print(b)

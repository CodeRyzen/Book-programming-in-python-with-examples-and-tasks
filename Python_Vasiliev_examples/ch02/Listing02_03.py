# Вводится число:
number=int(input("Введите число: "))
# Сообщение о первом делителе числа:
print("Делится на",1)
# Начальное значение для делителя:
k=1
# Поиск делителей числа:
while k<number//2:
    # Значение делителя увеличивается на единицу:
    k=k+1
    # Если k не является делителем числа:
    if number%k!=0:
        # Завершение текущего цикла:
        continue
    # Сообщение о делителе числа:
    print("Делится на",k)
# Сообщение о последнем делителе числа:
print("Делится на",number)

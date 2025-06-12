# Функция с вложенной функцией:
def mysum(*a):
    # Список:
    txt=["чисел","квадратов","кубов"]
    # Вложенная функция:
    def calc(n):
        s=0
        for m in range(len(a)):
            s+=a[m]**n
        return s
    # Вызов вложенной функции:
    for k in range(len(txt)):
        print("Сумма",txt[k]+":",calc(k+1))
# Вызов функции:
mysum(1,3,5,7)


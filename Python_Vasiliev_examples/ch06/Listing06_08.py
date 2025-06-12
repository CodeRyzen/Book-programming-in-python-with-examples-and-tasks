# Функции с произвольным количеством аргументов:
def sqr_sum(*n):
    s=0
    for a in n:
       s+=a*a
    return s
def get_sum(*n):
    s=0
    for a in n:
        if type(a)==int:
           s+=a
    return s
def get_text(*t):
    return " ".join(t)
# Вызов функций:
print("Сумма квадратов:",sqr_sum(1,3,5))
print("Сумма квадратов:",sqr_sum(2,4,6,8,10))
print("Сумма чисел:",get_sum(2,"A",4,"B",6))
print("Сумма чисел:",get_sum(1,[2,3],4))
print("Сумма чисел:",get_sum())
print("Текст:",get_text("Всем","привет"))
print("Текст:",get_text("A","B","C","D"))

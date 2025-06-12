# Импорт функций:
from copy import *
# Описание класса:
class MyClass:
    pass
# Создание объекта:
A=MyClass()
# Поля объекта:
A.value=100
A.nums=[1,2,3]
# Присваивание ссылки на объект:
B=A
# Копия объекта:
C=copy(A)
# Полная копия объекта:
D=deepcopy(A)
print("Созданы объекты")
# Поля объектов:
print("A:",A.value,"и",A.nums)
print("B:",B.value,"и",B.nums)
print("C:",C.value,"и",C.nums)
print("D:",D.value,"и",D.nums)
print("A.value=200 и A.nums[1]=0")
# Новые значения для полей:
A.value=200
A.nums[1]=0
# Поля объектов:
print("A:",A.value,"и",A.nums)
print("B:",B.value,"и",B.nums)
print("C:",C.value,"и",C.nums)
print("D:",D.value,"и",D.nums)
print("Удаляется A")
# Удаление переменой:
del A
print("B.value=300 и B.nums[2]=4")
# Новые значения для полей:
B.value=300
B.nums[2]=4
# Поля объектов:
print("B:",B.value,"и",B.nums)
print("C:",C.value,"и",C.nums)
print("D:",D.value,"и",D.nums)




# Создание списков:
A=[10,20,30]
print("A:",A)
B=["Python",[1,2]]
print("B:",B)
# Вычисление суммы списков:
C=A+B
print("C:",C)
# Добавление элемента в конец списка:
C+=[100]
print("C:",C)
# Удаление элемента списка:
C[1:2]=[]
print("C:",C)
# Добавление элемента в начало списка:
C=[200]+C
print("C:",C)
# Замена нескольких элементов в списке:
C[:3]=["A","B"]
print("C:",C)
# Вставка элементов в список:
C[2:2]=[8,9]
print("C:",C)
# Присваивание значения элементу списка:
C[2:3]=[7]
print("C:",C)

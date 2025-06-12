# Создание множеств:
A={2*k+1 for k in range(5)}
B={2*k for k in range(5)}
C={2*k+1 for k in range(3,8)}
# Содержимое множеств:
print("Созданы множества:")
print("A =",A)
print("B =",B)
print("C =",C)
# Объединение множеств:
print("Объединение множеств:")
print("A | B =",A.union(B))
print("B | A =",B.union(A))
print("A | C =",A|C)
# Пересечение множеств:
print("Пересечение множеств:")
print("A & B =",A.intersection(B))
print("A & C =",A&C)
# Разность множеств:
print("Разность множеств:")
print("A - C =",A-C)
print("C - A =",C.difference(A))
# Симметрическая разность множеств:
print("Симметрическая разность множеств:")
print("A ^ C =",A^C)
print("C ^ A =",C.symmetric_difference(A))
# Исходные множества:
print("Исходные множества:")
print("A =",A)
print("B =",B)
print("C =",C)

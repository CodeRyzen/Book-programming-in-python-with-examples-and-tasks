# Функции:
def alpha():
    print("Это Alpha!")
def bravo():
    print("Это Bravo!")
def hello():
    print("А это Hello!")
# Переменная с целочисленным значением:
num=123
# Вызов функций и проверка значения переменной:
print("Сначала было так:")
alpha()
bravo()
hello()
print("num =",num)
# Изменение значений:
alpha,bravo=bravo,alpha
num=hello
hello=321
# Вызов "функций" и проверка значения "переменной":
print("А стало так:")
alpha()
bravo()
num()
print("hello =",hello)

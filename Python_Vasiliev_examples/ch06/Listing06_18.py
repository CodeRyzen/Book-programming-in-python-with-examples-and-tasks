# Функция с аннотациями:
def show(txt:"Текст"="Функция show()")->"Результата нет":
    print(txt)
# Вызов функции:
show()
# Словарь аннотаций:
print(show.__annotations__)
# Аннотации:
for k in show.__annotations__:
    print(k,"-",show.__annotations__[k])

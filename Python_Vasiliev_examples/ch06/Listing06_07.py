# Значение по умолчанию для аргумента - список:
def show(val=[0,1,2]):
    for k in range(len(val)):
       val[k]+=1;
    print(val)
# Вызов функции:
show()
show()
show()

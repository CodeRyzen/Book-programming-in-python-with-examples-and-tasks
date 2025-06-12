# Класс со специальными методами:
class Alpha:
    # Метод для считывания значения по индексу:
    def __getitem__(self,index):
        return self.value[index]
    # Метод для присваивания значения по индексу:
    def __setitem__(self,index,val):
        self.value[index]=val
    # Метод для удаления по индексу:
    def __delitem__(self,index):
        del self.value[index]
    # Метод для приведения к тестовому формату:
    def __str__(self):
        return str(self.value)
    # Метод для вычисления "длины" объекта:
    def __len__(self):
        return len(self.value)
# Создание объекта:
A=Alpha()
# Поле-список для объекта:
A.value=[100,200,300]
# Проверка содержимого объекта:
print(A)
# Операции с объектом с использованием индекса:
for k in range(len(A)):
    print(A[k],end=" ")
print()
A[1]="A"
print(A)
del A[0]
print(A)

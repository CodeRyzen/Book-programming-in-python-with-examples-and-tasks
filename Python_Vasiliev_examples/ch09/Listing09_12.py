# Первый класс:
class Alpha:
    # Конструктор:
    def __init__(self,val):
        self.value=val
    # Метод для оператора "равно":
    def __eq__(self,val):
        print("Alpha: 'равно'")
        return self.value==val
    # Метод для оператора "не равно":
    def __ne__(self,val):
        print("Alpha: 'не равно'")
        return self.value!=val
    # Метод для оператора "меньше":
    def __lt__(self,val):
        print("Alpha: 'меньше'")
        return self.value<val
    # Метод для оператора "больше или равно":
    def __ge__(self,val):
        print("Alpha: 'больше или равно'")
        return self.value>=val
# Второй класс:
class Bravo:
    # Конструктор:
    def __init__(self,val):
        self.value=val
    # Метод для оператора "равно":
    def __eq__(self,val):
        print("Bravo: 'равно'")
        return self.value==val
# Создание объектов и выполнение сравнений:
A=Alpha(100)
print("Операции с объектом A")
print("[01] A==100:",A==100)
print("[02] A!=100:",A!=100)
print("[03] 200==A:",200==A)
print("[04] 200!=A:",200!=A)
print("[05] A<200:",A<200)
print("[06] 200>A:",200>A)
print("[07] A>=200:",A>=200)
print("[08] 100<=A:",100<=A)
B=Bravo(300)
print("Операции с объектом B")
print("[9] B==300:",B==300)
print("[10] B!=300:",B!=300)
print("[11] 400==B:",400==B)
print("Сравнение объектов A и B")
print("[12] A==B:",A==B)
print("[13] B!=A:",B!=A)
print("[14] A!=B:",A!=B)

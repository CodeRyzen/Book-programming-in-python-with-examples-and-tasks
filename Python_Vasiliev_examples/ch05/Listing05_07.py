txt=input("Введите текст: ")
symb=input("Какую букву найти? ")
num=txt.find(symb)
L=[]
while num!=-1:
    L.append(num)
    num=txt.find(symb,num+1)
if len(L)==0:
    print("Такой буквы в тексте нет!")
else:
    print(f"Позиции буквы '{symb}' в тексте: {L}")

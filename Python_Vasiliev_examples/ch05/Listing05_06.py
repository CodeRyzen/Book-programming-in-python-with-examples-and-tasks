txt=input("Введите текст: ")
symb=input("Какую букву найти? ")
num=txt.count(symb)
if num==0:
    print("Такой буквы в тексте нет!")
else:
    print(f"В тексте {num} букв(ы) '{symb}'")

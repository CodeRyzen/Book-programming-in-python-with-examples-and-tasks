# Считывается текст:
txt=input("Введите текст: ")
# Файл открывается для записи:
mf=open("D:\\Books\\Python\\mytext.txt",'w')
# Текст записывается в файл:
mf.write(txt)
# Закрывается файл:
mf.close()
# Сообщение о завершении копирования:
print("Текст записан в файл")

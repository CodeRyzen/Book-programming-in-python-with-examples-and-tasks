# Текстовый литерал без префикса:
A="\"Java\"\n\"Python\""
print(A)
print("Символов:",len(A))
# Текстовый литерал с префиксом:
B=r"\"Java\"\n\"Python\""
print(B)
print("Символов:",len(B))
# Переменная с текстовым значением:
name="Python"
# Текстовый литерал с префиксом:
C=f"Язык {name} - простой и понятный"
print(C)
C=f"Язык {name!r} - простой и понятный"
print(C)
# Переменная с числовым значением:
num=12.34567
# Текстовый литерал с префиксом:
txt=f"Число: {num:9.3f}"
print(txt)
txt=f"Число: {num:09.3f}"
print(txt)
# Новое числовое значение переменной:
num=42
# Формат для отображения целого числа:
txt=f"Число: {num:*>9d}"
print(txt)
# Формат для отображения шестнадцатеричного числа:
txt=f"Число: {num:#09x}"
print(txt)
txt=f"Число: {num:9x}"
print(txt)
txt=f"Число: {num:*<9x}"
print(txt)
# Формат для отображения восьмеричного числа:
txt=f"Число: {num:*^#09o}"
print(txt)
# Формат для отображения двоичного числа:
txt=f"Число: {num:#9b}"
print(txt)

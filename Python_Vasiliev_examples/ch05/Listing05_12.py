# Исходный текст:
txt=input("Ваш текст: ")
# Переменные:
new_txt=""
m=ord("а")
n=ord("я")
M=ord("А")
N=ord("Я")
# Создание шифра:
for s in txt:
    k=ord(s)
    if (k>=m and k<n) or (k>=M and k<N):
        s=chr(k+1)
    elif k==n:
        s=chr(m)
    elif k==N:
        s=chr(M)
    new_txt+=s
# Проверка результата:
print("Шифр:",new_txt)


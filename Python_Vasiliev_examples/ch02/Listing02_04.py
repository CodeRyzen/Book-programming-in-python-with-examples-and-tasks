number=int(input("Введите число: "))
k=1
while k<=number//2:
    if number%k==0:
        print("Делится на",k)
    k=k+1
print("Делится на",number)

print("Операции со списком чисел...")
try:
    nums=eval(input("Введите числовой список: "))
    print("Получено значение: "+str(nums))
    a=int(nums[0])
    b=int(nums[3])
    print(str(a)+"/"+str(b)+"="+str(a/b))
except ZeroDivisionError:
    print("ZeroDivisionError: попытка деления на ноль!")
except IndexError:
    print("IndexError: неверный индекс элемента!")
except:
    print("Что-то пошло не так!")
print("Завершение программы.")

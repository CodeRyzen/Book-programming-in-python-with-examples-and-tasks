print("Операции со списком чисел...")
# Контролируемый код:
try:
    nums=eval(input("Введите числовой список: "))
    print("Получено значение: "+str(nums))
    a=int(nums[0])
    b=int(nums[3])
    print(str(a)+"/"+str(b)+"="+str(a/b))
# Обработка исключений:
except ValueError:
    print("ValueError: ошибка при преобразовании!")
except ZeroDivisionError:
    print("ZeroDivisionError: попытка деления на ноль!")
except TypeError:
    print("TypeError: недопустимая операция!")
except IndexError:
    print("IndexError: неверный индекс элемента!")
except SyntaxError:
    print("SyntaxError: невозможно вычислить выражение!")
except NameError:
    print("NameError: неверный идентификатор!")
print("Завершение программы.")

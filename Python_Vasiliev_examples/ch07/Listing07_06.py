# Импорт класса из модуля:
from datetime import time
# Объект для реализации момента времени:
mytime=time(13,35,20)
# Проверка результата:
print("Время:",mytime)
# Использование полей объекта:
print("Часы:",mytime.hour)
print("Минуты:",mytime.minute)
print("Секунды:",mytime.second)
# Создание нового объекта на основе существующего:
newtime=mytime.replace(15,second=45)
# Проверка результата:
print("Время:",newtime)
# Создание нового объекта:
mytime=time.fromisoformat("12:34:56")
# Проверка результата:
print("Время:",mytime)

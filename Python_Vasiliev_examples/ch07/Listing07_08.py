# Импорт класса из модуля:
from datetime import datetime
# Объект для реализации даты и времени:
md=datetime(2019,10,22,13,27,45)
# Проверка результата:
print("Дата и время:",md)
# Использование полей объекта:
print("Год:",md.year)
print("Месяц:",md.month)
print("Число:",md.day)
print("Часы:",md.hour)
print("Минуты:",md.minute)
print("Секунды:",md.second)
# Определение дня недели:
print("День недели:",md.weekday())
print("День недели:",md.isoweekday())
# Дата:
d=md.date()
# Проверка результата:
print("Дата:",d)
# Время:
t=md.time()
# Проверка результата:
print("Время:",t)
# Создание нового объекта на основе существующего:
nd=md.replace(1985,day=3,second=15)
# Проверка результата:
print("Дата и время:",nd)
# Создание нового объекта:
nd=datetime.fromisoformat("1998-08-12 11:25:36")
# Проверка результата:
print("Новая дата и время:",nd)
# Объект для текущей даты и времени:
td=datetime.today()
# Проверка результата:
print("Сегодня и сейчас:",td)
# Разность дат:
delta=md-td
# Проверка результата:
print("Интервал времени:",delta)
print("Дни:",delta.days)
print("Секунды:",delta.seconds)
print("Интервал в секундах:",delta.total_seconds())

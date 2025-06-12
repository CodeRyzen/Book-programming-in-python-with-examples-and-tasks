# Импорт класса из модуля:
from datetime import date
# Объект для реализации даты:
myday=date(2019,10,22)
# Проверка результата:
print("Первая дата:",myday)
# Использование полей объекта:
print("Год:",myday.year)
print("Месяц:",myday.month)
print("Число:",myday.day)
# Определение дня недели:
print("День недели:",myday.weekday())
print("День недели:",myday.isoweekday())
# Создание нового объекта на основе существующего:
newday=myday.replace(1985,day=15)
# Проверка результата:
print("Вторая дата:",newday)
# Создание нового объекта:
newday=date.fromisoformat("1998-08-12")
# Проверка результата:
print("Новая дата:",newday)
# Объект для текущей даты:
thisday=date.today()
# Проверка результата:
print("Сегодня:",thisday)
# Разность дат:
delta=myday-thisday
# Проверка результата:
print("До первой даты:",delta)

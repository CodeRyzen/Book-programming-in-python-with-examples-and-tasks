# Список со значениями ключей:
days=["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
# Создание словарей:
week={days[s]:s for s in range(len(days))}
myweek={d:days.index(d) for d in days}
# Проверка результата:
print(week)
print(myweek)
# Создание еще одного словаря:
sqrs={k:k**2 for k in range(1,11) if k%2!=0}
# Проверка результата:
print(sqrs)

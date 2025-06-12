# Функция без аргументов не возвращает результат:
def next_day():
    txt=input("Какой сегодня день недели? ")
    txt=txt.lower().strip()
    if txt=="понедельник":
       new_txt="вторник"
    elif txt=="вторник":
       new_txt="среда"
    elif txt=="среда":
       new_txt="четверг"
    elif txt=="четверг":
       new_txt="пятница"
    elif txt=="пятница":
       new_txt="суббота"
    elif txt=="суббота":
       new_txt="воскресенье"
    elif txt=="воскресенье":
       new_txt="понедельник"
    else:
       print("Нет такого дня недели!")
       return
    print(f"Завтра - {new_txt}")
# Функция без аргумента возвращает результат:
def get_name():
    name=input("Добрый день! Как Вас зовут? ")
    if name.strip(" .,:;!?_")=="":
       name="Мистер Икс"
    return name
# Функция без аргументов не возвращает результат:
def hello():
    name=get_name()
    print(f"Приятно познакомиться, {name}!")
    next_day()
# Вызов функции:
hello()

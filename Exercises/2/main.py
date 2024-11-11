import datetime

current_year = datetime.date.today().year
birth_year = int(input("В каком году ты родился: "))
user_age = current_year - birth_year

print(f"Тебе сейчас:  {user_age - 1} - {user_age} лет")
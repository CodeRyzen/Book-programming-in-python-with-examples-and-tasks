import datetime

# User data
day = int(input("Day: "))
month = int(input("Month: "))

print("Your data: ", month, "-", day)

# Today
today = datetime.date.today()

print("Today: ", today)
from datetime import datetime

def get_user_birthday():
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))
    return datetime(datetime.now().year, month, day)

def calculate_days_until_next_birthday(birthday):
    now = datetime.now()
    next_birthday = datetime(now.year, birthday.month, birthday.day)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, birthday.month, birthday.day)
    return (next_birthday - now).days

user_birthday = get_user_birthday()
days_until_next_birthday = calculate_days_until_next_birthday(user_birthday)
print(f"Days until your next birthday: {days_until_next_birthday}")

import datetime as dt

# now = dt.datetime.now()
# print(now)
# year = now.year  #
# print(year)
# month = now.month
# print(month)
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# my_birthday = dt.datetime(year=1984, month=6, day=17, hour=4)
# print(my_birthday)

birthdays_dict = {
    'Machete': {
        'birthday': [2021, 3, 2],
        'email': 'machete@gmail.com'
    },
    'Yoyamenta': {
        'birthday': [1959, 1, 1],
        'email': 'elyoyo@yahoo.com'
    },
    'Boca de jaruco': {
        'birthday': [1988, 10, 10],
        'email': 'bocaciega_campismo@hotmail.com'
    }
}


def check_date():
    today = dt.datetime.now()
    today_formatted = f'{today.year}-{today.month}-{today.day}'
    for k, v in birthdays_dict.items():
        # print(v['birthday'])
        year = v['birthday'][0]
        month = v['birthday'][1]
        day = v['birthday'][2]
        birthday = dt.datetime(year=year, month=month, day=day)
        birthday_formatted = f'{birthday.year}-{birthday.month}-{birthday.day}'
        if today_formatted == birthday_formatted:
            return v['email']


print(check_date())

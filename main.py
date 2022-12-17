import smtplib
import datetime as dt
from random import choice

my_email = 'victorgrinan@gmail.com'  # victorgrinan@gmail.com vgsoftware.yahoo.com
password = 'tvwhwjmaxsxxczut'
address = 'victimaburro@yahoo.com'
msg = 'Hello\nThis is an automated email test.'

service_providers = {
    'gmail': "smtp.gmail.com",
    'hotmail': "smtp.live.com",
    'yahoo': "smtp.mail.yahoo.com",
    'Outlook': 'smtp-mail.outlook.com'
}

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


def auto_email(from_email, to_email, text):
    for provider in service_providers:
        if provider in from_email:
            with smtplib.SMTP(service_providers[provider], 465) as connection:
                connection.starttls()
                connection.login(user=from_email, password=password)
                connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=text)
        else:
            print('service provider not found')


def random_quote():
    with open('quotes.txt') as file:
        data = file.readlines()

    quote_list = [line.strip() for line in data]

    quote = choice(quote_list)
    return quote


def whos_birthday():
    today = dt.datetime.now()
    today_formatted = f'{today.year}-{today.month}-{today.day}'
    for k, v in birthdays_dict.items():
        year = v['birthday'][0]
        month = v['birthday'][1]
        day = v['birthday'][2]
        birthday = dt.datetime(year=year, month=month, day=day)
        birthday_formatted = f'{birthday.year}-{birthday.month}-{birthday.day}'
        if today_formatted == birthday_formatted:
            return v['email']


# auto_email(my_email, whos_birthday(), random_quote())
auto_email(my_email, my_email, random_quote())  # test code

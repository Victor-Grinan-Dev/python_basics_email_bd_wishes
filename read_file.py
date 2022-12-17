from random import choice


def random_quote():
    with open('quotes.txt') as file:
        data = file.readlines()

    quote_list = [line.strip() for line in data]

    quote = choice(quote_list)
    return quote

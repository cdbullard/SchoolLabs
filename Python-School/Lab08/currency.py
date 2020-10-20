def to_euro(dollar, exchange_rate=0.81):
    euro = dollar * exchange_rate
    return format(euro, '.2f')


def to_yen(dollar, exchange_rate=106.45):
    yen = dollar * exchange_rate
    return format(yen, '.2f')


def to_peso(dollar, exchange_rate=18.58):
    peso = dollar * exchange_rate
    return format(peso, '.2f')

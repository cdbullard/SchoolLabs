def parking_payment(hours, table):
    fee = 0
    tables = {
        "f1": 5.0,
        "f2": 4.0,
        "f3": 2.0
    }
    fee = int(tables[table] * hours)
    return fee


def table_selector(minutes):
    # if minutes do not equal a whole hour, round up to the next hour
    if minutes % 60 == 0:
        hours = int(minutes / 60)
    else:
        hours = int(minutes / 60 + 1)

    if hours <= 1:
        table = "f1"
        return dict(hours=hours, table=table)
    elif 1 < hours <= 5:
        table = "f2"
        return dict(hours=hours, table=table)
    elif hours > 5:
        table = "f3"
        return dict(hours=hours, table=table)
    else:
        raise RuntimeError("Something went wrong")


if __name__ == '__main__':
    m = 0
    try:
        m = int(input("Please enter number of minutes parked... "))
    # ask for user input again, if integer is less than 0 or a non-integer is mistakenly entered
    except ValueError:
        m = int(input("Please enter number of minutes parked as a positive integer... "))
        while m < 0:
            m = int(input("Please enter number of minutes parked as a positive integer... "))

    ts_out = table_selector(minutes=m)
    parking_fee = parking_payment(hours=ts_out["hours"], table=ts_out["table"])
    print(f"Parking fee for {m} minutes is ${parking_fee}")

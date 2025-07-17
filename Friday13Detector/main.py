import datetime


def detector(year=1999, month=1):
    datee = datetime.date(year, month, 13)
    _, _, weekday = datee.isocalendar()
    if weekday == 5:
        return True
    else:
        return False



month = int(input("insert Month "))
year = int(input("insert Year "))

hasFriday13 = detector(year, month)

if hasFriday13:
    print(f"{month}/{year} have a Friday 13")
else:
    print(f"{month}/{year} dont have a Friday 13")
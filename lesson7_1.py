import datetime as dt

newdate = input("Введите дату (dd.mm.yyyy)\n")
resdate = dt.datetime.strptime(newdate, "%d.%m.%Y").date()
days_7 = dt.timedelta(days=7)
result = resdate+days_7
print(result.strftime("%d.%m.%Y"))

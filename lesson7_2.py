import datetime as dt
from datetime import date
import calendar as cal

newyear = int(input("Введите год (yyyy)\n"))
calendar1 = cal.TextCalendar()
#new_cal = calendar1.pryear(newyear)
#print(new_cal)
mas = []
def sum_friday():
    return sum(cal.weekday(newyear, m, 13) == 4 for m in range(1, 13))
    res1 = sum(cal.weekday(newyear, m, 13) == 4 for m in range(1, 13))
    if res1 >0:
        pass
    else:
        print(f"Пятниц 13-е нет в {newyear} году")



def count_friday():
    for m in range(1, 13):
        element = dt.date(newyear, m,13)
        weekday = element.weekday()
        el = element.strftime("%d.%m.%Y")
        if weekday == 4:
            #print(f"Пятница 13-е: {element}"
            mas.append(el)
        else:
            pass




result = sum_friday()
result1 = count_friday()
print(f"Количество пятниц 13-е в {newyear} году: {result}")
print(f"Даты пятниц 13-е в {newyear} году:")
print(str(mas))

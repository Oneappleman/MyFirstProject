import math
class PiNum:
    num1 = math.pi
    print(num1)
    maxPi = int(round(math.pi, 13))




    def __init__(self):
        rou = int(input("Введи количество символов после запятой для числа пи: "))
        num1 = round(math.pi, rou)
        PiNum.num1 = num1
        print(num1)
        #PiNum.maxPi = round(math.pi, 13)







    #@property
    #def maxPi(self):
    #    return PiNum.maxPi
    #@maxPi.setter
    #def x(self):
     #   print("Изменение запрещено")

    #@maxPi.deleter
    #def x(self):
    #    print("Удаление запрещено")


    def __str__(self):
        return f"Текущее значение числа пи: {str(self)}"

    #def __int__(self):
     #   return f"Максимальное значение числа пи: {self}"






PiNum()
print(PiNum.__str__(PiNum.num1))
print(PiNum.__str__(PiNum.maxPi))
#print(PiNum.__int__(PiNum.maxPi))

print(type(PiNum.maxPi))



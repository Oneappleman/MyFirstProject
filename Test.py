class TriangleChecker:
    num1 = ""
    num2 = ""
    num3 = ""

    #def __init__(self, num1, num2, num3):
        #self.num1 = input("Напиши число для длинны одной стороны треугольника: ")
        #self.num2 = input("Напиши число для длинны второй стороны треугольника: ")
        #self.num3 = input("Напиши число для длинны третьей стороны треугольника: ")
        #self.line2 = line23

        #self.line3 = line3

    def is_triangle(num1, num2, num3):
        if type(num1) == str:
            print("Нужно вводить только числа!")
        else:
            pass
        if isinstance(num2, int) == True:
            pass
        else:
            print("Нужно вводить только числа!")
        if isinstance(num3, int) == True:
            pass
        else:
            print("Нужно вводить только числа!")
        if (num1 > 0):
            pass
        else:
            print("С отрицательными числами ничего не выйдет!")
        if (num2 > 0):
            pass
        else:
            print("С отрицательными числами ничего не выйдет!")
        if (num3 > 0):
            pass
        else:
            print("С отрицательными числами ничего не выйдет!")
        if (num1+num2) < num3:
            print("Жаль, но из этого треугольник не сделать")
        else:
            print("Ура, можно построить треугольник!")

   # def numbers(self):
    #    num1 = input("Напиши число для длинны одной стороны треугольника: ")
    #    num2 = input("Напиши число для длинны второй стороны треугольника: ")
     #   num3 = input("Напиши число для длинны третьей стороны треугольника: ")
    #numbers()

TriangleChecker.num1 = input("Напиши число для длинны одной стороны треугольника: ")
TriangleChecker.num2 = input("Напиши число для длинны второй стороны треугольника: ")
TriangleChecker.num3 = input("Напиши число для длинны третьей стороны треугольника: ")
TriangleChecker.is_triangle(TriangleChecker.num1, TriangleChecker.num2, TriangleChecker.num3)

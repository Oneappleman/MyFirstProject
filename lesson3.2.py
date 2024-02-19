class TriangleChecker:

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self, a, b, c):
        while True:
            a = TriangleChecker.a
            try:
                a = int(a)
                break
            except ValueError:
                print("Нужно вводить только числа!")
                break
        while True:
            b = TriangleChecker.b
            try:
                b = int(b)
                break
            except ValueError:
                print("Нужно вводить только числа!")
                break

        while True:
            c = TriangleChecker.c
            try:
                c = int(c)
                break
            except ValueError:
                print("Нужно вводить только числа!")
                break
        if (a > 0):
            pass
        else:
            print("С отрицательными числами ничего не выйдет!")
        if (b > 0):
            pass
        else:
            print("С отрицательными числами ничего не выйдет!")
        if (c > 0):
            pass
        else:
            print("С отрицательными числами ничего не выйдет!")

        if (a+b) < c:
            print("Жаль, но из этого треугольник не сделать")
        else:
            print("Ура, можно построить треугольник!")

TriangleChecker.a = input("Напиши число для длины одной стороны треугольника: ")
TriangleChecker.b = input("Напиши число для длины второй стороны треугольника: ")
TriangleChecker.c = input("Напиши число для длины третьей стороны треугольника: ")
TriangleChecker(TriangleChecker.a, TriangleChecker.b, TriangleChecker.c)
TriangleChecker.is_triangle("",TriangleChecker.a, TriangleChecker.b, TriangleChecker.c)








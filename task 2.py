num = int(input("Write number: "))
a = str(bin(num))
b = str(oct(num))
c = str(hex(num))
print(f"""Bin= {a}
Oct= {b}
Hex= {c}""")
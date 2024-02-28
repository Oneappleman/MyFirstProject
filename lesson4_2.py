file2 = open("Телефоны.txt", "w")
table = []
index=0
street = input("Write street: ")
house = input("Write house: ")
flat = input("Write flat: ")
num = input("Write tel number: ")
table.append(street)
table.append(house)
table.append(num)
ost = 0
with open("Телефоны.txt", "w") as file:
    for i in range(0,10):
        if index == 10:
            table.clear()
            street = input("Write street: ")
            house = input("Write house: ")
            flat = input("Write flat: ")
            num = input("Write tel number: ")
            #table.append(street)
            #table.append(house)
            #table.append(num)
            file2.write(f"{index+1}\t {table}\n")
            index +=1
        else:
            ost = 10-index
            print(f"Осталось ввести еще данных в количестве: {ost}")
            table.clear()
            street = input("Write street: ")
            house = input("Write house: ")
            flat = input("Write flat: ")
            num = input("Write tel number: ")
            #table.append(street)
            #table.append(house)
            #table.append(num)
            file2.write(f"{index + 1}\t {street}\t {house}\t {flat}\t {num}\n")
            index += 1


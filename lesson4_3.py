#file2 = open("Телефоны.txt", "r")
print("Write tel number: ")
word = input()
#f = file2.read()
#file2.close()

with open("Телефоны.txt") as file:
    lines = file.readlines()
    last_line = lines[-1]
    for line in lines:
        if word in line:
            print(f"Строка найдена:")
            print(line)
            break
        else:
            if line == last_line:
                print("Строка не найдена!")
            else:
                pass
        file.close()
    #content = file.read()

    #print(lines)
    #file.close()
file1 = open("text4lesson4.txt", "w")
num = []
cube = []
quad = []
for i in range (0,101):
    num.append(i)
    cube.append(i**2)
    quad.append(i**3)
    if i != 0:
            #print(num[i], cube[i], quad[i])
            file1.write(f"{num[i]}, {cube[i]}, {quad[i]} \n")
    else:
        pass




#file1 = open("text_lesson4.txt", 'w') as file:
#print(num)
#print(cube)
#print(quad)
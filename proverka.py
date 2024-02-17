input_list= ['1','2','3','4','5']
res1= input_list[0]/2
res2= input_list[1]/2
res3= input_list[2]/2
res4= input_list[3]/2
res5= input_list[4]/2
res_list = [res1,res2,res3,res4,res5]
complex_list = []
float_list = []
def proverka():
    for i in input_list:
        input_list[i] +=1
        if isinstance(i,float):
            float_list.append(i)
        else:
            complex_list.append(i)
print(input_list)
print(complex_list)
print(float_list)
S = str(input("Write word: "))

def sfunc(arg: [str])  -> str:
    pos = 0
    sep = "-*-"
    result = ''
    n=0
    while n<len(arg):
        n += 1
        result += arg[pos] +sep
        pos += 1
    return result


#print(sfunc(S))
sfunc(S)
print(sfunc(S))










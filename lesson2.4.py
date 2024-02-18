S = str(input("Write some text: "))
def slen(arg: [str]) -> str :
    word = arg.split()
    wlength = len(word)
    slength = len(arg.replace(" ", ""))
    return wlength, slength
slen(S)
print(slen(S))



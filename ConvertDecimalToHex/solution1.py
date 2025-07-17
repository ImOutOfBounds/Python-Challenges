# In this solution, i tryed to minimize the size of the code

def solution1(word="teste"):
    letters = list(word.lower())
    res = ""

    for i in letters:
        res += str(hex(ord(i))) + " "

    print(res)

solution1()
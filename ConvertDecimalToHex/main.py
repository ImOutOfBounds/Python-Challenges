alp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
hexSeq = ['A', 'B', 'C', 'D', 'E', 'F']

def findHex(ch):

    isNum = True
    j = 0
    k = 0
    l = 0

    for i in ch:
        if isNum: 
            val = j
            j += 1
        else: 
            val = hexSeq[k]
            k += 1

        ch[i] = [str(ch[i]), str(6 + l % 2) + str(val)]

        if j == 10 or k == 6:
            isNum = not isNum
            j = 0
            k = 0
            l += 1
    
    return ch

def solution1(word="teste"):
    letters = list(word.lower())
    res = ""

    for i in letters:
        res += str(hex(ord(i))) + " "

    print(res)


def solution2(word="teste"):
    ch = {}
    j = 96
    wordL = list(word.lower())

    for i in alp:
        ch[i] = j
        j += 1

    for i in wordL:
        pass
    
    
    print(findHex(ch))



solution2()

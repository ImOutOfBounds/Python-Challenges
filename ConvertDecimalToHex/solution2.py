# in this solution, i tryed to use more logic to built the function, using less python built in functions, such as hex() and ord() 

alp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
hexSeq = ['A', 'B', 'C', 'D', 'E', 'F']

def findHex(ch):

    isNum = True
    j = 0
    k = 0
    l = 0
    start = 6

    for i in ch:
        if isNum: 
            val = j
            j += 1
        else: 
            val = hexSeq[k]
            k += 1

        ch[i] = [str(ch[i]), str(start) + str(val)]

        if j == 10 or k == 6:
            isNum = not isNum
            j = 0
            k = 0
            l += 1
        
        if l > 1:
            start = 7
    
    return ch


def solution2(word="teste"):
    ch = {}
    j = 96
    wordL = list(word.lower())

    for i in alp:
        ch[i] = j
        j += 1

    hexDict = findHex(ch)
    res = ''
    for i in wordL:
        res += "0x" + hexDict[i][1] + " "
    
    print(res)
    
    
solution2()
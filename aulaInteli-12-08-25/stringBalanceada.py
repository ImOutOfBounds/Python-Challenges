def isBalanced(inp: str) -> bool:

    res = []
    for i in range(len(inp)):
        if(inp[i] == '(' or inp[i] == '[' or inp[i] == '{'):
            res.append(inp[i])
        if(inp[i] == ')'):
            if res[-1] == '(':
                res.remove(-1)
        if(inp[i] == ']'):
            if res[-1] == '[':
                res.remove(-1)
        if(inp[i] == '}'):
            if res[-1] == '{':
                res.remove(-1)
       
    print(res)
    if len(res) == 0:
        True
    else: 
        return False


print(isBalanced("(vai corinthians)"))
# F(n) = F(n-1) + F(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonnacci(res: int) -> int:
    fib = []
    for i in range(res):
        if i == 0 or i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib[-1]


print(fibonnacci(133))
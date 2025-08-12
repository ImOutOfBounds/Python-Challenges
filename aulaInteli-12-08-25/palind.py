def isPalind(s: str) -> bool:
    sRerverse = ''
    for i in range(len(s)):
        sRerverse += s[-(i+1)]
    return sRerverse == s


print(isPalind("aabbaa"))
print(isPalind("aabb"))
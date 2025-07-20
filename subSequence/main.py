def subSequence(s: str, t: str) -> bool:
    finalR = ''
    j = 0
    for i in t:
        if j >= len(s):
            break
        if i == s[j]:
            finalR += s[j]
            j += 1

    return finalR == s

test_cases = {
    1: {"expected": True, "s": "ace", "t": "abcde"},
    2: {"expected": False, "s": "aec", "t": "abcde"},
    3: {"expected": True, "s": "", "t": "abcde"},
    4: {"expected": True, "s": "abc", "t": "ahbgdc"},
    5: {"expected": False, "s": "axc", "t": "ahbgdc"},
    6: {"expected": True, "s": "leandro", "t": "lleaaxnnzzddrrrooo"},
    7: {"expected": False, "s": "leandro", "t": "lean"},
    8: {"expected": True, "s": "a", "t": "abc"},
    9: {"expected": False, "s": "abc", "t": ""},
    10: {"expected": True, "s": "abc", "t": "aabbcc"},
}

for i, case in test_cases.items():
    result = subSequence(case["s"], case["t"])
    print(f"Test {i}: Expected: {case['expected']} | Result: {result} | s: '{case['s']}' | t: '{case['t']}'")

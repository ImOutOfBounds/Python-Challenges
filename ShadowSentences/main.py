def shadowSentences(sentence1="they are round", sentence2="fold two times") -> bool:

    sentlist1 = sentence1.split(" ")
    sentlist2 = sentence2.split(" ")

    if len(sentlist1) != len(sentlist2):
        return False
    

    for i in range(len(sentlist1)):
        sent1L = list(sentlist1[i])
        sent2L = list(sentlist2[i])

        if len(sent1L) !=  len(sent2L):
            return False
        
        for j in sent1L:
            for k in sent2L:
                if j == k:
                    return False

    return True


test_cases = {
    1: {"expected": True, "s1": "vai mano", "s2": "bom lele"},
    2: {"expected": False, "s1": "his friends", "s2": "our company"},
    3: {"expected": True, "s1": "they are round", "s2": "fold two times"},
    4: {"expected": False, "s1": "hello world", "s2": "great stone"},
    5: {"expected": False, "s1": "fast run", "s2": "slow jog"},
    6: {"expected": True, "s1": "big red", "s2": "low sun"},
    7: {"expected": False, "s1": "my house", "s2": "in boxes"},
    8: {"expected": True, "s1": "cat bed", "s2": "jug rim"},
    9: {"expected": False, "s1": "look here", "s2": "good view"},
    10: {"expected": True, "s1": "win the war", "s2": "jug fix mop"},
}


for i, case in test_cases.items():
    result = shadowSentences(case["s1"], case["s2"])
    print(f"Test {i}: Expected: {case['expected']} | Result: {result} | Sentence 1: '{case['s1']}' | Sentence 2: '{case['s2']}'")
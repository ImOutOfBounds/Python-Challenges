def findDifferentLetter(word1="lweordtest1", word2="etanworstddr1o") -> str:
    wordList1 = list(word1)
    wordList2 = list(word2)

    wordList1copy = wordList1.copy()


    for i in range(len(wordList1)):
        for j in range(len(wordList2)):
            if wordList1[i] == wordList2[j]:
                wordList1copy.remove(wordList1[i])
                wordList2.remove(wordList2[j])
                break
    
    res = wordList1copy + wordList2

    return ''.join(res)


print(findDifferentLetter())
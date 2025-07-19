def duplicateLetterCheck(word) -> bool:

    letters = list(word)

    for i in range(len(letters)):
        for j in range(len(letters)):
            if letters[i] == letters[j] and i != j:
                print(letters[i])
                return True

    return False



print(duplicateLetterCheck("teste"))
print(duplicateLetterCheck("nice"))
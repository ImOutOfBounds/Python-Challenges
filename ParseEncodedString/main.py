def parseCode(code):

    first_name, last_name, id = code.split("000")
    res = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id
    }

    return res

print(parseCode('Leandro000Custodio000789'))
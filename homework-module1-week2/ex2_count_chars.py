def count_chars(word:str) -> dict:
    """COunt each character in a word"""
    result = {}

    for i in word:
        if result.get(i) == None:
            result[i] = 1
        else:
            result[i] += 1

    return result

# string = 'Happiness'
# print(count_chars(string))
# string = 'smiles'
# print(count_chars(string))

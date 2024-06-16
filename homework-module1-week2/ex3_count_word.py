def count_word(file_path: str)->dict:
    """count number of apperance of a word in text find"""
    result = {}

    file = open("content\P1_data.txt", "r")
    content = file.read()
    content = content.replace('\n', ' ')
    content = content.split(' ')
    for word in content:
        if result.get(word) == None:
            result[word] = 1
        else:
            result[word] += 1

    return result

file_path = '/content/P1_data.txt'
result = count_word ( file_path )
print ( result)
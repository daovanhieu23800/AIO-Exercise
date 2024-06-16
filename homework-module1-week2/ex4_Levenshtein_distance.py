
def Levenshtein_distance(source:str, target:str)-> int:
    """Metric to calculate the difference between 2 string. This metric will calculate the minimum changes of source so that source == target"""
    result = 0

    matrix = [[0] * (len(target)+1) for i in range(len(source)+1)]

    for i in range(len(source)+1):
        matrix[i][0] = i  
    for i in range(len(target)+1):
        matrix[0][i] = i  

    for i in range(1,len(source)+1):
        for j in range(1,len(target)+1):
            if source[i-1] == target[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1

    result = matrix[len(source)][len(target)]

    return result       

print(Levenshtein_distance('yu', 'you'))
print(Levenshtein_distance('hi', 'hello'))
print(Levenshtein_distance('hola', 'hello'))
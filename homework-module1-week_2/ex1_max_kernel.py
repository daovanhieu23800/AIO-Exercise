def max_kernel(num_list:list, k: int) -> list[int]:
    """Find max in slide_window with length K"""
    assert k>=1 , """k need to greater than 1"""

    result = []
    for i in range(len(num_list)-k+1):
        max_number = max(num_list[i:i+k])
        result.append(max_number)
    
    return result

# print(max_kernel([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1], k=3))
# print(max_kernel([3 , 4 , 5 , 1 , -44] , 3))
# print(max_kernel([3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1], k=3))
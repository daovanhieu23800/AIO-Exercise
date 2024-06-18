def factorial(n: int) -> int:
    """calculate factorial"""
    assert type(n) is int, "n must be integer number"
    result = 1
    for i in range(1, n+1):
        result *= i        
    return result


def approx_sin(x: float, n: int)->float:
    """calculate sin using approximation"""
    result = 0
    for i in range(n+1):
        result += ((-1)**i) * ((x**(2*i+1)) / factorial(2*i+1))
    return result

def approx_cos(x: float, n: int)->float:
    """calculate cos using approximation"""
    result = 0
    for i in range(n+1):
        result += ((-1)**i) * ((x**(2*i)) / factorial(2*i))
    return result

def approx_sinh(x: float, n: int)->float:
    """calculate sinh using approximation"""
    result = 0
    for i in range(n+1):
        result += ((x**(2*i+1)) / factorial(2*i+1))
    return result


def approx_cosh(x: float, n: int)->float:
    """calculate cosh using approximation"""
    result = 0
    for i in range(n+1):
        result += ((x**(2*i)) / factorial(2*i))
    return result


# print(approx_sin ( x =3.14 , n =10))
# print(approx_cos ( x =3.14 , n =10))
# print(approx_sinh ( x =3.14 , n =10))
# print(approx_cosh ( x =3.14 , n =10))

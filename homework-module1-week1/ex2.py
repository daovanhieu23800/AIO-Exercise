import math

def is_number (n) -> bool :
    """Checking input is number or not"""
    try :
        float (n) # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    
    return True

def calculate_activation(x:float, activation_func_name: str) -> float:
    """Calculate activation function base on input and type of activation func"""

    assert is_number(x) == True , "x must be a number"
    x = float(x)
    print(f"Input x = {x}")
    print(f"Input activation Function ( sigmoid | relu | elu ) : {activation_func_name}")

    result = 0
    if activation_func_name == "relu":
        if x <= 0:
            result = 0
        else: 
            result = x

    elif activation_func_name == "sigmoid":
        result = 1.0/(1.0 + math.e**(-x))

    elif activation_func_name == "elu":
        alpha = 0.01
        if x <= 0:
            result = alpha * (math.e**(x)-1)
        else: 
            result = x

    else:
        raise ValueError(f"{activation_func_name} is not supported")

    print(f"{activation_func_name} : f ({x}) = {result}")
    return result

# calculate_activation(1,'relu')
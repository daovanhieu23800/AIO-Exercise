import random
import math
random.seed(227)

def calculate_regression_loss(n: int, loss_name_func:str) -> float:
    """calculate loss for regression model"""
    result = 0
    assert type(n) is int, "number of samples must be an integer number"
    print(f"Loss function name: {loss_name_func}")

    for i in range(n): 
        current_loss = 0
        y_hat = random.uniform(0,10)
        y = random.uniform(0,10)

        if loss_name_func == 'MAE':
            current_loss =  abs(y_hat-y)
        elif loss_name_func == 'MSE':
            current_loss =  abs(y_hat-y)**2
        elif loss_name_func == 'RMSE':
            current_loss =  math.sqrt(abs(y_hat-y)**2)
        else:
            print(f"{loss_name_func} is not supported")
            break
        
        print(f"loss name : {loss_name_func} , sample : {i} , pred : {y_hat} , target : {y} ,loss : {current_loss}")
        result += current_loss
    print(f"final {loss_name_func} : {result}")
    return result


# calculate_regression_loss('aa', 'MAE')
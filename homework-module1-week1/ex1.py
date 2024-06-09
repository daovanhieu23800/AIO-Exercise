def evaluate_classification_model(tp: int, fp:int , fn:int) -> float:
    """This func is to calculate precision, recall, F1 score of classification model"""

    #checking type 
    assert type(tp) is int, "tp must be int"
    assert type(fp) is int, "fp must be int"
    assert type(fn) is int, "fn must be int"

    # checking value
    assert (tp > 0) and (fp > 0) and (fn > 0) , "tp and fp and fn must be greater than zero"
    
    precision = float(tp / (tp + fp))
    recall = float(tp / (tp + fn))
    f1_score = float(2 * (precision * recall) / (precision + recall))

    print(f"Precision is: {precision}")
    print(f"Recall is: {recall}")
    print(f"F1-score is: {f1_score}")
    return precision, recall, f1_score

#print(evaluate_classification_model(2,3,4))
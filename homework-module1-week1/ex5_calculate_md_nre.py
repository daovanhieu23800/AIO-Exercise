def calculate_md_nre(y:float, y_hat: float, n:int, p:int)->float:
    """calculate Mean Difference of nth Root Error loss """
    loss = 0

    loss = (pow(y, (1/n)) - pow(y_hat, (1/n)))**p

    return loss

# print(calculate_md_nre ( y =100 , y_hat =99.5 , n =2 , p =1))
# print(calculate_md_nre ( y =50 , y_hat =49.5 , n =2 , p =1))
# print(calculate_md_nre ( y =20 , y_hat =19.5 , n =2 , p =1) )
# print(calculate_md_nre ( y =0.6 , y_hat =0.1 , n =2 , p =1))
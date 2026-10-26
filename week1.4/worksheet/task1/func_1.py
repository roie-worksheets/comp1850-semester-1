
def func_1(lst_value): 
    ''' 
    Returns the average of a list size `lst_value`
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 
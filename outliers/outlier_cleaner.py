#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    count = 0
    to_del = int(0.1*len(ages))
    temp = {}
    for i in range(len(net_worths)):
        error = abs(predictions[i] - net_worths[i])
        temp[(ages[i][0],net_worths[i][0])] = error

    key_sort = sorted(temp, key=temp.get, reverse=True)
    ### your code goes  here
    for i in key_sort:
        if count <= to_del:
            temp.pop(i)
            count+=1
        else:
            break
    
    for i in temp.keys():
        cleaned_data.append((i[0],i[1],temp[i]))
    return cleaned_data


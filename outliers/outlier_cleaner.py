#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np

    cleaned_data = []

    ### your code goes here
    residual_error = np.absolute(np.add(predictions,[x * (-1) for x in net_worths]))
    cleaned_data = [(x, y, z) for z,x,y in sorted(zip(residual_error,ages,net_worths), reverse=True)]
    
    percentage = int(len(cleaned_data)*0.1)
    cleaned_data = cleaned_data[percentage:]

    return cleaned_data


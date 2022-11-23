def sumvalues(values):
    """Your documentation goes here"""    
    total = 0
    for x in values:
        if type(x) is int or type(x) is float:
            total += x
        else:
            return 'NON INT Error'
    return total


def maxvalue(values):
    """Your documentation goes here"""
    max_num = min
    for x in values:
        if type(x) is int or type(x) is float:
            if x > max_num:
                max_num = x
        else:
            return 'NON INT Error'
    return max_num


def minvalue(values):
    """Your documentation goes here"""
    min_num = max
    for x in values:
        if type(x) is int or type(x) is float:
            if x < min_num:
                min_num = x
        else:
            return 'NON INT Error'
    return min_num


def meannvalue(values):
    """Your documentation goes here"""
    num_of_values = 0
    for x in values:
        num_of_values += 1
    total = sumvalues(values)
    if type(total) is int:
        mean_value = (total / num_of_values).__round__(4)
        return mean_value
    else:
        return total


def countvalue(values, xw):
    """Your documentation goes here"""
    counter = 0
    for x in values:
        if x == xw:
            counter += 1
    return counter

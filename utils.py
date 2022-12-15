def sumvalues(values):
    """Your documentation goes here"""    
    total = 0
    for x in values:
        try:
            total += x
        except TypeError:
            raise TypeError('Incorrect parameter type')
        except Exception:
            raise Exception('Other error Encountered')
    return total


def maxvalue(values):
    """Your documentation goes here"""
    max_num = -1000
    for x in values:
        try:
            if x > max_num:
                max_num = x
        except TypeError:
            raise TypeError('Incorrect parameter type')
        except Exception:
            raise Exception('Other error Encountered')
    return max_num


def minvalue(values):
    """Your documentation goes here"""
    min_num = 100000
    for x in values:
        try:
            if x < min_num:
                min_num = x
        except TypeError:
            raise TypeError('Incorrect parameter type')
        except Exception:
            raise Exception('Other error Encountered')
    return min_num


def meannvalue(values):
    """Your documentation goes here"""
    num_of_values = 0
    for x in values:
        num_of_values += 1
    try:
        total = sumvalues(values)
        mean_value = round((total / num_of_values), 4)
    except TypeError:
        raise TypeError('Incorrect parameter type')
    except Exception:
        raise Exception('Other error Encountered')
    return mean_value


def countvalue(values, xw):
    """Your documentation goes here"""
    counter = 0
    for x in values:
        if x == xw:
            counter += 1
    return counter

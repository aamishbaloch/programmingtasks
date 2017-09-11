def is_power(base_number, number_to_check):
    x = number_to_check/base_number
    if x == base_number:
        return True
    elif x > base_number:
        return is_power(base_number, x)
    else:
        return False


def is_power_2(number_to_check):
    return number_to_check != 0 and ((number_to_check & (number_to_check - 1)) == 0)

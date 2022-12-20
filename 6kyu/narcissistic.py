def narcissistic(value):
    digits = str(value)
    return value == sum(int(d)**len(digits) for d in digits)
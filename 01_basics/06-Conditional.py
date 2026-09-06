def absolute(x):
    """Compute Abs of x"""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x
result = absolute(-7)
print(result)

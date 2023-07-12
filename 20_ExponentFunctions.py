def raiseTo (base, power): 
    result = 1
    for index in range(power): result *= base
    return result

print(raiseTo(5, 2))
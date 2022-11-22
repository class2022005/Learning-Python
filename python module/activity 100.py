def complexity(password):
    res = 0b00000000
    for c in password:
        if len(password) >= 15:
            res |= 0b1
        if c.isdigit():
            res |= 0b10
        if c.isupper():
            res |= 0b100
        if c.islower():
            res |= 0b1000
        if not c.isalnum():
            res |= 0b10000
    return res

print(complexity('J0sh1saGassaTH$NG'))
# Given a linux file mode (permissions) as an integer, return the permission string that the mode represents.

# Example 1:
# mode = 511 
# 511 == 0b111111111
# permissons = 'rwxrwxrwx'

# Example 2:
# mode = 424
# 424 == 0b110101000
# permissions = 'rw-r-x---'
def perms(mode):
    res = ''
    t = f'{mode:09b}'
    for i, n in enumerate(t):
        if n == "1":
            if int(i) % 3 == 0:
                res += 'r'
            if int(i) % 3 == 1:
                res += 'w'
            if int(i) % 3 == 2:
                res += 'x'
        else:
            res += '-'
    return res

mode = 511
print(perms(mode))
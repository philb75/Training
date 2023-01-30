def dig_pow(n, p):
    digits = [int(x) for x in str(n)]
    total = 0
    for i in range(len(digits)):
        total += digits[i] ** (p + i)
    if total % n == 0:
        return total // n
    else:
        return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))
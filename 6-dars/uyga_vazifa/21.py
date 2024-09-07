def rim_nums(s):
    rim = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    n = 0
    for c in s[::-1]:
        value = rim[c]
        if value < n:
            total -= value
        else:
            total += value
        n = value
    return total

print(rim_nums("XXVII"))

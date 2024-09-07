lst = [100, 200, 305, 400]
filtered = sorted([x for x in lst if str(x).count('0') >= 2])

print(filtered)

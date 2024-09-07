for i in range(1, 1001):
    son = int(str(i)[::-1])
    boluvchi = 1
    sum = 0
    while boluvchi <= son//2:
        if not son %boluvchi:
            sum +=boluvchi
        boluvchi += 1
    if son == sum:
        print(i,son)

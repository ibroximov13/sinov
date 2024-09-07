lst = ['Olma', 'Uzum', 'anor', 'nok', 'behi']
for i in lst:
    # print(i)
    for a in i:
        # print(a)
        if a == 'm':
            print(i[::-1],end = ' ')
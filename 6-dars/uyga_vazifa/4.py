def mus_man(n):
    if n > 0:
        return -n
    else:
        return 2 * -n

lst = [1, 32, -3, -4]
teskari = list(map(mus_man, lst))

print(teskari)

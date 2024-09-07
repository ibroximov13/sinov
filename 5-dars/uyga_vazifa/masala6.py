def func(son: int) -> int:
    son = str(son)
    natija = ""

    for raqam in son:
        if raqam == '6':
            natija += '9'
        elif raqam == '9':
            natija += '6'
        else:
            natija += raqam

    return int(natija[::-1]) == son

son = int(input("Sonni kiriting: "))
natija = func(son)
print(natija)
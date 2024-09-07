def func(ranglar: list) -> int:
    last_color = ranglar[0]
    sekund = 0

    for rang in ranglar:
        if rang == last_color:
            sekund += 2
        else:
            sekund += 3
            last_color = rang

    return sekund

ranglar = ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Red']
natija = func(ranglar)

print(natija)
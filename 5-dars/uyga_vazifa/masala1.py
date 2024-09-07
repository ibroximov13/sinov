def func (lst: list) -> list:
    natija = []

    for son in lst:
        natija.append([son] * len(lst))

    return natija

lst = list(input("Nimadir kiriting: "))
print(func(lst))
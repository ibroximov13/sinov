def func(gap: str) -> str:
    lst = gap.split(" ")
    natija = ""
    for soz in lst:
        if len(soz) < 4:
            natija += "*" * len(soz)
        else:
            natija += soz
        natija += " "
    return natija
gap  = input("Gap kiriting: ")

print(func(gap))
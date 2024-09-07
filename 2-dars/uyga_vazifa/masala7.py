soat = int(input("Soat = "))
minut = int(input("Minut = "))

if minut >= 45:
    minut -= 45
else:
    minut = minut + 60 - 45
    if soat == 0:
        soat = 23
    else:
        soat -= 1

print(f"{soat}:{minut:02d}")

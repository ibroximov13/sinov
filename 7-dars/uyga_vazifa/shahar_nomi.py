from os import system
from json import dumps
system("clear")
fayl = open("languages1.txt","r")
shaharlar = fayl.read().split("\n")
natijalar = []
for i in range(len(shaharlar)):
    shahar = shaharlar[i].split(',')

    natija = {
        'shahar_nomi': shahar[0],
        'aholi_soni': int(shahar[1]),
        'tili': shahar[2]
    }
    natijalar.append(natija)
print(dumps(natijalar, indent=4))
aholi_1m = []
for shahar in natijalar:
    if shahar['aholi_soni'] > 1000000:
        aholi_1m.append(shahar)
print("Aholi soni 1mln dan katta bolganlari",dumps(aholi_1m,indent=4))


fayl.close()
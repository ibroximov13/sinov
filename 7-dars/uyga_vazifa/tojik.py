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
for i in natijalar:
    if i['tili'] == 'Tajik':
        print(i)

fayl.close()
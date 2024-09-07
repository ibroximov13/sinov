fayl = open("salom.txt", "w")
soz = "Salom nima gap Qalesiz"
sozlar = soz.split()
for word in sozlar:
    if len(word) > 4:
        fayl.write(word + "\n")


fayl.close
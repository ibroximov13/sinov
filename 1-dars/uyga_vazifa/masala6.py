soz = input("So'z kiriting: ")

uzunlik = len(soz) #salom dunyo --> kiritsa uzunligi 11 ga teng
""" print(uzunlik)
print(soz[uzunlik//2:]) # kiritilgan sozlardi yarmidan keyingisini olish
print(soz[:uzunlik//2]) """ # kiritilgan sozlardi yarmidan oldingisini olish
natija = soz[uzunlik//2:] + ' ' + soz[:uzunlik//2] 
print("Natija:", natija)

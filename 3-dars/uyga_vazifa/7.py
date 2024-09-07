sozlar = ["katta-kichik","aka-uka","ota-ona","opa-singil"]
birinchilari = []
ikkinchilari = []
for i in sozlar:
    birinchilari.append(i.split('-')[0])
    ikkinchilari.append(i.split('-')[1])
print(sozlar)
print(birinchilari)
print(ikkinchilari)
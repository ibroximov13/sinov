natija = 0
while True:
    son = input("Son kiriting: ")

    if son.isdigit():
        natija +=int (son)
    else:
        break
print(natija)

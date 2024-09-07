n = int(input("Son kiriting: "))
def manfiy():
    global n
    if n < 0:
        return True
    else:
        return False

natija = manfiy()
print(natija)
n = input("Son kiriting: ")
sum = 1
last = 0
num = 0
uzunlik = len(n)
for i in range (uzunlik):
    if (int(n[i]) % 2 == 1):
        print(n[i])
    
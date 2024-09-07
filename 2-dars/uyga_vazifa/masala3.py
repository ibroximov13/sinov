son = int(input("Son kiriting: "))
ikkilik = ''
while(0 < son):
    ikkilik += str(son%2)
    son = son//2
print(ikkilik[::-1])

print(type(ikkilik))

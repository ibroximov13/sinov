lst = []
nat = []
for i in range(1,11):
    lst.append(i)
    if isinstance(i,int):
        i = "Salom"
        nat.append(i)
print(lst)
print(nat)


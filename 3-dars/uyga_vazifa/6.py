import random
lst1 = []
lst2 = []
new_lst = []
n = int(input("N ni kiriting: "))

for i in range(n):
    random_son = random.randint(1,10)
    random_son2 = random.randint(1,10)
    lst1.append(random_son)
    lst2.append(random_son2)
print("List1 = ",lst1)
print("List2 = ",lst2)
for j in lst1:
    if j % 2 == 0:
        kv = j*j
        lst2.append(kv)
print("Natija: list2 =",lst2)
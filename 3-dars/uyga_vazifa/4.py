import random
lst = []
new_lst = []
n = int(input("N ni kiriting: "))

for i in range(n):
    random_son = random.randint(1,100)
    lst.append(random_son)
print("List:",lst)

for j in lst:
    if j % 3 == 0 and j % 5 == 0:
        new_lst.append(j)
        new_lst.sort()
        
print("Yangi list:",new_lst)
# print(len(new_lst))
# print(type(len(new_lst)))

if len(new_lst) >= 2 :
    new_lst.reverse()
    teskari = new_lst.copy()
    print("Natija:",teskari)
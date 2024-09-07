import random
lst = []
toq_sonlar = []
juft_sonlar = []
n = int(input("N ni kiriting: "))

for i in range(n):
    random_son = random.randint(1,100)
    lst.append(random_son)
print("List:",lst)

for j in lst:
    if not j % 2 == 0:
        toq_sonlar.append(j)
        toq_sonlar.sort()
        # print(j)
    else: 
        juft_sonlar.append(j)
        juft_sonlar.sort()
print("Toq sonlar:",toq_sonlar)
print("Juft sonlar:",juft_sonlar)
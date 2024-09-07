lst = []
for i in range(1,10+1):
    if i % 2 == 0:
        # print(i)
        lst.append(i)
print(lst)
n = int(input("Son kiritng: "))
lst.append(n)
lst.sort()
# print(lst)
print(lst.index(n))
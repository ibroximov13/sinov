son = int(input("Son kiriting: "))
second_son = 0
third_son = 0

for i in range(1,son):
    if not son % i:
        second_son+=i
for i in range(1,second_son):
    if not second_son % i:
        third_son+=i
if(son == third_son):
    print("do'stona son")
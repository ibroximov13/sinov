son = int(input("5 xonali son kiriting: "))
count = 0
while son !=0: 
    last = son % 10
    son //= 10
    count +=last
print("Natija:",count)
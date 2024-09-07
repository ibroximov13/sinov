N = int(input("Son kiriting: "))
lst = [1, 2, 5, 10, 235, 34]
son = list(filter(lambda x: x > N**3, lst))

print(son)

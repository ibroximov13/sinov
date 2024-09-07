son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if ((son1 % 2 == 0 and son2 % 2 != 0) or (son1 % 2 != 0 and son2 % 2 == 0)) and (son1 % 3 == 0 and son2 % 3 == 0):
    print("TRUE")
else:
    print("FALSE")

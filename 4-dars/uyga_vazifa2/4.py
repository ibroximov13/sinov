Sample_Dictionary = {0: 10, 1: 20}
Expected_Result = {}
s = 0
lst = list()

for k,v in Sample_Dictionary.items():
    s += v 
lst.append(s)
print(lst)
Expected_Result = Sample_Dictionary.copy()

print(tuple(lst))
print(Expected_Result)
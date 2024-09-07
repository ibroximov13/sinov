set1 = {'olma', 'anor', 'behi', 'uzum', 'banan'}
set2 = {'banan', 'anjir', 'uzum', 'gilos', 'olma', 'behi'}
set3 = set()
set1.intersection_update(set2)
set3.update(set1)
print(set3)

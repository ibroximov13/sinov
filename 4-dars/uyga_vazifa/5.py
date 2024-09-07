st1 = {'olma', 'anor', 'behi', 'uzum', 'banan'}
st2 = {'banan', 'anjir', 'uzum', 'gilos', 'olma', 'behi'}
strr = ''
st1.intersection_update(st2)
for i in st1:
    strr += i + ' '
print(strr)
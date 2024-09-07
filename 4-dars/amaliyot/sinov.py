st1 = {'oltin', 'olma', 'duo', 'ol'}
st2 = {'olma', 'anor', 'behi', 'uzum', 'nok', 'anjir'}
strr = ''
natija = st1.difference(st2)
for i in natija:
    strr += i + ' '
print(strr,)
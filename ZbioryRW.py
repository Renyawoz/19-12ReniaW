zbior = {1,2,3,6,7,8}
oceny = [5,4,3,4,3,2,6,1,3,6,2,]
nowe_oceny = set(oceny)
print(nowe_oceny.intersection(zbior))
print(nowe_oceny.difference(zbior))
print(zbior.difference(nowe_oceny))
#print(nowe_oceny)


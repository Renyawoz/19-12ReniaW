słownik = {"klucz":"wartość"}

oceny = {
    "Juzio":[2,3,5,4,6],
    "Staś":[5,4,2,3,6,2],
    "Tomek":{'python':[4,5,3,2],
             'java':[3,5,3,6]}
}

print(oceny)
print(oceny['Juzio'])
print(oceny['Juzio'][:3])
print(oceny['Tomek'])
print(oceny['Tomek']['java'])
print(oceny['Tomek']['java'][:2])
print(oceny.items())
print(oceny.keys())
print(oceny.values())
print('Juzio' in oceny.keys())
print('3' in oceny.keys())
oceny['Dawid']=3
print(oceny)









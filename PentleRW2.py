lista = [4, 6, 8, 0]
wyniki = []
for i in lista:
    wyniki.append(i*20)

print(wyniki)

for i in range (5):
    print(i)

for i in range(100,200,50):
    print(i)


liczby = list(range(1,11,2))
print(liczby)

imiona = ['Stefan','Yeti', 'Babel', 'Genio']
lata = [25,26,28]
# for p in range(len(imiona)):
#     print(p, imiona[p])

# for poz,imie in enumerate(imiona):
#     wiek = lata[poz]
#     print(imie, wiek)

for person, age in zip(imiona,lata):
    print(person, age)
import random

#indeks = int(input('Podaj miejsce wstawienia:'))
#cyfra = input('Podaj ocenę z klasówki:')

oceny = [5,4,3,4,3,2,6,1,3,6,2,]
#print(len(oceny))
#print(oceny[:5])
print("Ilość trójek w ocnach", oceny.count(3))
print(oceny)
#oceny.insert(5, cyfra)

oceny.append(6)
oceny.remove(5)
oceny.pop(4)
oceny.sort()
oceny.reverse()
oceny[-1] = 4
print(oceny)
dziennik = tuple(oceny)
print(dziennik)

oceny2 = oceny.copy()
oceny2[-1]=33
print("oceny2", oceny2)
print(oceny)
loteria = random.choice(oceny)
print("Wylosowana liczba z tabeli ocen:",loteria)

kostka6 = random.randint(1,6)
print("Wynik rzutu kością:", kostka6)
print(random.random())








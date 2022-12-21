def squares(n):
    for x in range(n):
        wynik = x ** 2
    return wynik


def squares_gen(n):
    for x in range(n):
        yield x ** 2
sq = squares_gen(4)

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))

def counter (start =0):
    n = start
    while True:
        yield n
        n +=1



c = counter(100)
lista = [next(c),next(c), 2023,next(c),next(c), 2022 ]
print(lista)
print(next(c))
for i in range(next(c), 110):
        print(i)

c.close()
c.send()
print(f"Kolejna interakcja:{next(c)}")


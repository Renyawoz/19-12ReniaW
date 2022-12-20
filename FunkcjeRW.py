def drukuj_napis():
    print("RENIA")


drukuj_napis()


def drukarka(tekst, ile_razy):
    wydruk = (tekst + " ") * ile_razy
    return wydruk


lista = [drukarka("RENIA", 10), drukarka("RENIA", 5), drukarka("RENIA", 2), drukarka("RENIA", 10), 'YETI']
print(lista)

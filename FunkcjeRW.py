def drukuj_napis():
    print("RENIA")


drukuj_napis()


def drukarka(tekst, ile_razy):
    wydruk = (tekst + " ") * ile_razy
    return wydruk

def drukarka2(tekst, ile_razy):
  return  (tekst + " ") * ile_razy


lista = [drukarka("RENIA", 10), drukarka2("RENIA", 5), drukarka("RENIA", 2), drukarka("RENIA", 10), 'YETI']
print(lista)

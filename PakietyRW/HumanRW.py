from PakietyRW.klasyRW import Human


#
# def dodaj(a, b):
#     return a + b
#
# def odejmij(a, b):
#     return a - b
#
# def pomnoz(a, b):
#     return a * b

czlowiek1 = Human("Renia",18,'k')
# czlowiek1.imie = "Renia"
# czlowiek1.wiek = 18
# czlowiek1.plec = 'k'

czlowiek1.witaj()
czlowiek1.spacer()
czlowiek1.policz(4,7)





czlowiek2 = Human("Jasio", 19,'m')
# czlowiek2.imie = "Jasio"
# czlowiek2.wiek = 19
# czlowiek2.plec = 'm'

czlowiek2.witaj()
czlowiek2.spacer()
czlowiek2.policz(33,5)


czlowiek3 = Human("Ala",5,'k')
# czlowiek3.imie = "Ala"
# czlowiek3.wiek = 5
# czlowiek3.plec = 'k'

czlowiek3.witaj()
czlowiek3.spacer()
czlowiek3.policz(3,5)


czlowiek4 = Human(wiek=14)
# czlowiek4.imie = "Ala"
# czlowiek4.wiek = 5
# czlowiek4.plec = 'k'

czlowiek4.witaj()
czlowiek4.spacer()
czlowiek4.policz(3,5)
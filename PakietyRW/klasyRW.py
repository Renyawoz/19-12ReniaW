# class Human:
#
#     imie = ""
#     wiek = 0
#     plec = ""
#
#     def witaj(self):
#         print(f"Czesc, mama na imię {self.imie}")
#
#     def spacer(self):
#         if self.plec == 'k':
#             print('Poszlam na spacer')
#         else:
#             print('Pooszedlem na spacer')
#
#     def policz(self):
#         if self.wiek <7:
#             print('Nie potrafie jeszcze liczyc')
#         else:
#             print("2+2=4")
#     def policz(self):
#         if self.wiek <7:
#             print('Nie potrafie jeszcze liczyc')
#         else:
#             print("Wynik dodawania =",a+b)



class Human:



    def __init__(self, imie,wiek,plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec


    def witaj(self):
        print(f"Czesc, mama na imię {self.imie}")
    def spacer(self):
        if self.plec == 'k':
            print('Poszlam na spacer')
        else:
            print('Pooszedlem na spacer')

    # def policz(self):
    #     if self.wiek <7:
    #         print('Nie potrafie jeszcze liczyc')
    #     else:
    #         print("2+2=4")
    def policz(self):
        if self.wiek <7:
            print('Nie potrafie jeszcze liczyc')
        else:
            print("Wynik dodawania=", a +b )
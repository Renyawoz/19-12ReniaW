class Human:

    imie = ""
    wiek = 0
    plec = ""

    def witaj(self):
        print(f"Czesc, mama na imię {self.imie}")

    def spacer(self):
        if self.plec == 'k':
            print('Poszlam na spacer')
        else:
            print('Pooszedlem na spacer')

    def policz(self):
        if self.wiek <7:
            print('Nie potrafie jeszcze liczyc')
        else:
            print("22+2=4")

from PakietyRW.BankomatRW import BankomatRW

start_bal = float(input('Podaj wysokość salda:'))
savings = BankomatRW(start_bal)

pay = float(input('Podaj kwotę wpłaty:'))
print("Wpłacam środki...")
savings.despoit(pay)

cash = float(input("Podaj kwotę wypłaty:"))
print('Kwota zostanie odjęta od salda')
savings.pin(cash)

print(savings)

# saldo = savings.get_balance()
# print("Aktualne saldo rachunku wynosi", saldo)
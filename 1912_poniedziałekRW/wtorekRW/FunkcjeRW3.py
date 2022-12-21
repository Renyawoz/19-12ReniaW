def funkcja(x):
    return x * 2


fun = lambda x: x * 2

print(f"wynik dzialania funkcji {funkcja(5)}")
print(f"wynik dzialania funkcji {funkcja(20)}")
print(f"wynik dzialania funkcji {funkcja(3)}")
print(f"wynik dzialania funkcji {fun(9)}")
print(f"wynik dzialania funkcji {(lambda x: x * 2)(35)}")

wiek = lambda x: "dziecko" if x<10 else ("nastolatek" if x<18 else "dorosły")
print(wiek(5))
print(wiek(15))
print(wiek(30))

def mnozenie(a,b):
    try:
        return int(a)*int(b)
    except TypeError:
        return 0
    except ValueError:
        return "Blednie wprowadzone dane!"



def mnozenie2(a,b):
    try:
        return int(a)*int(b)
    except (TypeError,ValueError):
        return "Blednie wprowadzone dane!"

def mnozenie3(a,b):
    try:
        return int(a)*int(b)
    except Exception as e:
        return f"Wystapil blad :{e.args}"

print(mnozenie(3,4))
print(mnozenie("5","6"))
print(mnozenie("a","b"))
# #plik = open('klienci.txt','r')
# #plik =open('klienci.txt','w')
# plik = open('klienci.txt' , 'a')

with open('klienci.txt','a') as plik:
    plik.write("Renia")
with open('klienci.txt','r') as plik:
    nowa_lista=[]
    imie = plik.readline().rstrip('\n')
    while imie!="":
        nowa_lista.append(imie)
        imie = plik.readline().rstrip("\n")

# lista =['Genowefa','Ziuta']
# name = 'Stefania Janik'
# wiek = 41
#
# plik.write(name + "\n")
# # plik.write(str(wiek)+ "\n")
# # plik.write(str(lista)+ "\n")
#
# nowa_lista = []
# zawartosc1 = plik.readline().rstrip('\n')
# zawartosc2 = plik.readline().rstri('\n')
# zawartosc3 = plik.readline().rstrip('\n')
# zawartosc4 = plik.readline().rstrip('\n')
#
# nowa_lista.append(plik.readline() .rstrip('\n'))
# nowa_lista.append(plik.readline() .rstrip('\n'))
# nowa_lista.append(plik.readline() .rstrip('\n'))
# nowa_lista.append(plik.readline() .rstrip('\n'))
#
#
#
#
# plik.close()
print(nowa_lista)
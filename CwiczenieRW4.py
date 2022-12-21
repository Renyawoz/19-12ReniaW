import csv

# with open(r'C:\Users\CSComarch\Documents\19-12ReniaW\1912_poniedziałekRW\dane\osoby.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     licznik = 0
#     for row in csv_reader:
#         if licznik == 0:
#             print(f'Nazwy kolumn to{", ".join(row)}')
#             licznik +=1
#         else:
#             print(f'\t{row[0]}|\t{row[1]}|\t{row[2]}')
#             licznik += 1
#             print(f'Znalazłem{licznik}linii')

# with open(r'C:\Users\CSComarch\Documents\19-12ReniaW\1912_poniedziałekRW\dane\osoby.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     licznik = 0
#     for row in csv_reader:
#         if licznik == 0:
#             print(f'Nazwy kolumn to{", ".join(row)}')
#             licznik +=1
#         print(f"\t{row['name']}|\t{row['department']}|\t{row['birthday month']}")
#         licznik += 1
#     print(f'Znalazłem{licznik}linii')

with open(r'C:\Users\CSComarch\Documents\19-12ReniaW\1912_poniedziałekRW\dane\osoby.csv','a', newline="\n") as file:
    writer = csv.writer(file, delimiter=",", quoting = csv.QUOTE_MINIMAL)
    writer.writerow(['Renia', 'IT', 'Czerwiec'])


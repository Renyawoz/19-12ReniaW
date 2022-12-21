import json

with open(r'/1912_poniedziałekRW/dane/hero.json') as f:
    data = json.load(f)

print(data)

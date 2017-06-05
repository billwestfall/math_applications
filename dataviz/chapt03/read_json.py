import json

with open('nobel_winners.json') as f:
    nobel_winners = json.load(f)

print(nobel_winners)

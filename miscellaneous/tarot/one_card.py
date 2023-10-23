import random

a=(random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "Page", "Knight", "Queen", "King", "Ace"]), random.choice(["Swords", "Cups", "Coins", "Wands"]), random.choice(["Natural", "Reversed"]))
b=random.choice(["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]), random.choice(["Natural", "Reversed"]))
print(random.choice(a, b))

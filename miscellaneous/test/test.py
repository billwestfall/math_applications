import random

cardList = ["Ace \[ClubSuit]", "9 \[ClubSuit]", "10 \[ClubSuit]", "Jack \[ClubSuit]", "Queen \[ClubSuit]", "King \[ClubSuit]", "Ace \[SpadeSuit]", "9 \[SpadeSuit]", "10 \[SpadeSuit]", "Jack \[SpadeSuit]", "Queen \[SpadeSuit]", "King \[SpadeSuit]", "Ace \[DiamondSuit]", "9 \[DiamondSuit]", "10 \[DiamondSuit]", "Jack \[DiamondSuit]", "Queen \[DiamondSuit]", "King \[DiamondSuit]", "Ace \[HeartSuit]", "9 \[HeartSuit]", "10 \[HeartSuit]", "Jack \[HeartSuit]", "Queen \[HeartSuit]", "King \[HeartSuit]"]

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14)) 

nobel_winners = [{"category": "Physics","name":"Albert Einstein","nationality":"Swiss","sex":"male","year":1921},{"category":"Physics","name":"PaulDirac","nationality":"British","sex":"male","year":1933},{"category":"Chemistry","name":"Marie Curie","nationality":"Polish","sex":"female","year":1911}]

import dataset

db = dataset.connect('sqlite:///nobel_prize.db')

wtable = db['winners']
wtable.find()

with db as tx:
    tx['winners'].insert(w)
    
list(db['winners'].find())


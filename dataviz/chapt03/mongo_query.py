from pymongo import MongoClient

client = MongoClient()
db = clean.nobel_prize
coll = db.winners
res = coll.find({'category':'Chemistry'})
list(res)

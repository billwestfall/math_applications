from pymongo import MongoClient

client = MongoClient()
db = nobel_prize
coll = db.winners
res = coll.find({'category':'Chemistry'})
list(res)

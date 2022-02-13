import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.test
for item in db.restaurants.find():
    print(item["cuisine"])

import pymongo

client = pymongo.MongoClient("localhost", 27017)

collection = client.test.restaurants

for item in collection.find():
         print(item["cuisine"])


import pymongo

client = pymongo.MongoClient("localhost", 27017)

collection = client.test.restaurants

for item in collection.find({"address.zipcode":"11201"}):
         print(item)


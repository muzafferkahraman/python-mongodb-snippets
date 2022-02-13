import pymongo

client = pymongo.MongoClient("localhost", 27017)

mycol = client["test"]["muzo"]

myquery={ "name" : "muzo" }

newvalues = { "$set": { "age": "48" } }

x = mycol.update_one(myquery, newvalues)

print(x.modified_count)


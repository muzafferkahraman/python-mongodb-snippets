import pymongo

client = pymongo.MongoClient("localhost", 27017)

mycol = client["test"]["muzo"]

x = mycol.insert_one({ "name" : "muzo","age" : "44" })

print(x.inserted_id)

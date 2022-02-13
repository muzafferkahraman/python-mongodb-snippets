import pymongo

client = pymongo.MongoClient("localhost", 27017)

mycol = client["test"]["muzo"]

x = mycol.delete_one({ "name" : "muzo" })

print(x.deleted_count)

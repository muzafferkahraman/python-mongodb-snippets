import pymongo
client = pymongo.MongoClient("localhost", 27017)

mydb = client["test"]
mycol = mydb["muzo"]

x = mycol.delete_one({ "name" : "valentina" })

print(x.deleted_count)

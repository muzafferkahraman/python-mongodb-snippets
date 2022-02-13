import pymongo

D={}
ref=[]

client = pymongo.MongoClient("localhost", 27017)
db = client.test
for item in db.restaurants.find():
        if item["cuisine"] not in ref:
            ref.append(item["cuisine"])
            D.update({item["cuisine"]:1})
        else:
            t=D.get(item["cuisine"])
            t += 1
            D.update({item["cuisine"]:t})

D=sorted(D.items(), key=lambda kv: kv[1])
D.reverse()
D=dict(D)

for key in D:
        print(key.ljust(70,"."),D.get(key))

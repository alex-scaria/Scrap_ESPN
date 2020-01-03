import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["MotoGP"]

x = mycol.insert_many(moto_dict)

for j in mycol.find():
    print(j)
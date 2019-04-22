import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print("ID of X:")
print(x.inserted_id)

print("Names:")
print(myclient.list_database_names())
print(mydb.list_collection_names())

x = mycol.find_one()
print("Print first customer")
print(x)


import pymongo
import certifi

mongo_url = "mongodb+srv://aerebho13:Woodie13!@cluster0.seuco.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("KudosMeals")
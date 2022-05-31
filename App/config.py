from pymongo import MongoClient

client = MongoClient("mongodb+srv://db_admin:VO0usJYgofYmc6is@cluster0.lnt3z.mongodb.net/?retryWrites=true&w=majority")
db = client.test
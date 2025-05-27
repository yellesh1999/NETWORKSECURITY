import collections
import collections.abc

# Patch missing attributes in collections for Python 3.10+
for attr in ['Mapping', 'Sequence', 'MutableMapping']:
    if not hasattr(collections, attr):
        setattr(collections, attr, getattr(collections.abc, attr))

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://yelleshdeshmukh26:pasword@cluster0.gdwzqvy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.emadb
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

#Step 2: Create a collection into the DB
posts = db.posts
#pprint(collection)

#tento di pulire la collezione per un maggiore ordine e provo questa istruzione
# ncollec = posts.count()
# for j in range (1, ncollec):
#     posts.find_one_and_delete({'type':"1"})
posts.delete_many({'type':"1"})

#discutere sul fatto che i record possono essere replicati (non c'e un controllo a monte usando questo codice)
for i in range (1, 5):
    #Step 3: Create a document
    post = {"id": i,
            "type": "1",
            "tags": ["1", "22", "54"],
            }
    #Step 4: Insert a document
    post_id = posts.insert_one(post).inserted_id
    #pprint(db.collection_names(include_system_collections=False))

#Step 5: Find one document and count
#pprint(posts.find_one())
pprint(posts.find_one({'id':1}))
pprint(posts.find_one({'id':2}))
print(posts.find_one({'id':3}))
pprint(posts.find_one({'id':4}))
pprint(posts.find_one({'id':5}))
count = posts.find({'type':"1"}).count()
pprint(count)

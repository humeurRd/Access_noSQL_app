from pymongo import MongoClient
try:
    user = 'root'
    pwd ='1234'
    client = MongoClient(f'mongodb://{user}:{pwd}localhost')

    db = client.myDB
    collection = db.data

    objeto_1 = {
        'name':'objeto random',
        'description' : 'es sólo mío',
        'phrase' : 'mi precioso'
    }
    objeto_2 = {
        'name':'objeto random2',
        'description' : 'es sólo mío2',
        'phrase' : 'mi precioso2'
    }
    objeto_3 = {
        'name':'objeto random3',
        'description' : 'es sólo mío3',
        'phrase' : 'mi precioso3'
    }


    collection.insert_many([objeto_1, objeto_2, objeto_3])

    results = collection.find()
    for r in results:
        print(r)

except Exception as e:
    print(f'Error: {format(e)}')
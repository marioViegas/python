from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['test-database']
courses = db.courses

course = {
    'author': 'mario.viegas',
    'course': 'MongoDB Tutorial',
    'price': 100,
    'rating': 5
}

result = courses.insert_one(course)

if result.acknowledged:
    print('Course Added. The course Id id ' + str(result.inserted_id))

import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['SeriesDB']
# series_collection = db['series']
series_collection = db['films']


def insert_document(data, collection=series_collection):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


def find_document(elements, collection=series_collection, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


def update_document(query_elements, new_values, collection=series_collection):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(query, collection=series_collection):
    """ Function to delete a single document from a collection.
    """
    collection.delete_one(query)

# new_show = {
#     "name": "FRIENDS",
#     "year": 1994
# }
# print(insert_document(new_show, series_collection))
#
# result = find_document({'name': 'FRIENDS'}, series_collection)
# print(result)
#
# new_show = {
#     "name": "FRIENDS",
#     "year": 1995
# }
# id_ = insert_document(new_show, series_collection)
# update_document({'_id': id_}, {'name': 'F.R.I.E.N.D.S'}, series_collection)
#
# result = find_document({'_id': id_}, series_collection)
# print(result)
#
# delete_document({'_id': id_}, series_collection)
#
# result = find_document({'_id': id_}, series_collection)
# print(result)

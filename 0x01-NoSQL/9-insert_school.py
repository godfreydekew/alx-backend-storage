#!/usr/bin/env python3
'''
inserts a new document in a collection
'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs'''

    for key, value in kwargs.items():
        mongo_collection.insert_one({key: value})

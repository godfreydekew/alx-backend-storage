#!/usr/bin/env python3
'''
List all documents in Python
'''


def list_all(mongo_collection):
    '''lists all documents in a collection'''
    if mongo_collection.count_documents({}) != 0:
        return mongo_collection.find()
    return []

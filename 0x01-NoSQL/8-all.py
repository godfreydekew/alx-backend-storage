#!/usr/bin/env python3
'''
List all documents in Python
'''

def list_all(mongo_collection):
    if mongo_collection.count_documents({}) != 0:
        return mongo_collection.find()
    return []

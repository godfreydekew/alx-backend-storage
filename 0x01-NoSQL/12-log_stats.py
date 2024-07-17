#!/usr/bin/env python3
'''12. Log stats'''
from pymongo import MongoClient


if __name__ == "__main__":
    '''rovides some stats about Nginx logs stored in MongoDB'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    stats = client.logs.nginx
    x = stats.count_documents({})
    get = stats.count_documents({"method": "GET"})
    post = stats.count_documents({"method": "POST"})
    put = stats.count_documents({"method": "PUT"})
    patch = stats.count_documents({"method": "PATCH"})
    delete = stats.count_documents({"method": "DELETE"})
    status = stats.count_documents({"path": "/status"})
    print(f"{x} logs")
    print("Methods:")
    print(f"    method GET: {get}")
    print(f"    method POST: {post}")
    print(f"    method PUT: {put}")
    print(f"    method PATCH: {patch}")
    print(f"    method DELETE: {delete}")
    print(f"{status} status check")

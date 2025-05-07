#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB.
It connects to a MongoDB instance running on localhost at port 27017
and retrieves logs from the 'nginx' collection in the 'logs' database.
It counts the total number of logs and the number of logs for each HTTP method
(GET, POST, PUT, PATCH, DELETE).
It also counts the number of logs with the path '/status'.
"""


from pymongo import MongoClient


def log_stats():
    """
    Connects to MongoDB and retrieves stats about Nginx logs.
    Prints the total number of logs and the number
    of logs for each HTTP method.
    Also prints the number of logs with the path '/status'.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    path = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()

#!usr/bin/env python3
"""
Module to list all documents in a MongoDB collection"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents in the collection
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return list(mongo_collection.find())

#!/usr/bin/env python3
"""
Module to insert a new document in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object
        kwargs: keyword arguments to insert in the document

    Returns:
        The new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

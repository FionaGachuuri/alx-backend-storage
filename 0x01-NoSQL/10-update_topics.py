#!/usr/bin/env python3
"""
Module to update topics of a school document in a MongoDB collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school document in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object
        name (string): school name to update
        topics (list of strings): list of topics approached in the school

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

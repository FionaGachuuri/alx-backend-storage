#!/usr/bin/env python3
"""
Module to find schools by topic in a MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find schools by topic in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object
        topic (string): topic to search for

    Returns:
        List of schools with the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))

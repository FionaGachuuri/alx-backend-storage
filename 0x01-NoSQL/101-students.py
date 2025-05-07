#!/usr/bin/env python3
"""
This module provides a function to retrieve students
sorted by their average score.
"""


def top_students(mongo_collection):
    """
    Connects to MongoDB and retrieves students sorted by their average score.
    Returns a list of dictionaries containing student
    names and their average scores.
    The list is sorted in descending order based on the average score.
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])

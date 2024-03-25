#!/usr/bin/env python3
"""Module makes use of pymongo."""


def schools_by_topic(mongo_collection, topic):
    """
    Function returns list of school
    having a specific topic.
    """
    return (mongo_collection.find({ "topics": topic }))


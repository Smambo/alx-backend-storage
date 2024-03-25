#!/usr/bin/env python3
"""This module uses pymongo"""


def update_topics(mongo_collection, name, topics):
    """
    Function changes all topics of a
    school docment based on the name.
    """
    mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })

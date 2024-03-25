#!/usr/bin/env python3
"""
Below function inserts a new document
in a collection based in kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new '_id'
    """
    id_object = mongo_collection.insert_one(kwargs)
    return (id_object.inserted_id)

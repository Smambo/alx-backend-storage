#!/usr/bin/env python3
"""
Below function lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    Returns list of all documents in the collection,
    otherwise an empty list if no doc exists.
    """
    collection_obj = mongo_collection.find()

    return [document for document in collection_obj]

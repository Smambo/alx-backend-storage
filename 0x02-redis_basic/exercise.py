#!/usr/bin/env python3
"""Import modules for Redis data storage"""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    """
    Class represents object for Redis data storage
    """
    def __init__(self) -> None:
        """Initialises class instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in Redis data storage and returns a key"""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return (data_key)

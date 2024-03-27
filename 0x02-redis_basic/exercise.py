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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Gets value from Redis data storage"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Gets string value from Redis data storage"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Gets an integer value from Redis data storage"""
        return self.get(key, lambda x: int(x))

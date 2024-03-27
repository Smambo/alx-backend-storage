#!/usr/bin/env python3
"""Import modules for Redis data storage"""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """
    Counts how many times methods of Cache class are called.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Invokes given method after incrementing call counter.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return (method(self, *args, **kwargs))
    return (invoker)


def call_history(method: Callable) -> Callable:
    """
    Stores the history of inputs and outputs for
    a particular function
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Returns method output after storing its
        inputs and output.
        """
        input_key = '{}:inputs'.format(method.__qualname__)
        output_key = '{}:outputs'.format(method.__qualname__)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_key, str(args))
        
        output = method(self, *args, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(output_key, output)
        return (output)
    return (invoker)


class Cache:
    """
    Class represents object for Redis data storage
    """
    def __init__(self) -> None:
        """Initialises class instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
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

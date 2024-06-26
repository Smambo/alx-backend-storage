## Redis basic <br>
![image](https://github.com/Smambo/alx-backend-storage/assets/113464914/090212c8-fe55-42f5-95f4-666a2b93d9a3) <br>

### Learning Objectives
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

### Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Tasks: <br>
[0. Writing strings to Redis](./exercise.py)<br>
Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int` or `float`.<br>
```
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic# cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic# python3 main.py
91d87db8-18b3-4455-bc36-ad2c85ee2546
b'hello'
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic#
```

[1. Reading from Redis and recovering original type](./exercise.py)<br>
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store `"a"` as a UTF-8 string, it will be returned as `b"a"` when retrieved from the server.

In this exercise we will create a `get` method that take a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.

The following code should not raise:<br>
```
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

[2. Incrementing values](./exercise.py)<br>
Familiarize yourself with the `INCR` command and its python equivalent.

In this task, we will implement a system to count how many times methods of the `Cache` class are called.

Above `Cache` define a `count_calls` decorator that takes a single `method` `Callable` argument and returns a `Callable`.

As a key, use the qualified name of `method` using the `__qualname__` dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

Remember that the first argument of the wrapped function will be `self` which is the instance itself, which lets you access the Redis instance.

Protip: when defining a decorator it is useful to use `functool.wraps` to conserve the original function’s name, docstring, etc. Make sure you use it as described [here](https://docs.python.org/3.7/library/functools.html#functools.wraps).

Decorate `Cache.store` with `count_calls`.<br>
```
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic# cat 2-main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic# ./2-main.py
b'1'
b'3'
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic#
```

[3. Storing lists](./exercise.py)<br>
Familiarize yourself with redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc.

In this task, we will define a `call_history` decorator to store the history of inputs and outputs for a particular function.

Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.

In `call_history`, use the decorated function’s qualified name and append `":inputs"` and `":outputs"` to create input and output list keys, respectively.

`call_history` has a single parameter named `method` that is a `Callable` and returns a `Callable`.

In the new function that the decorator will return, use `rpush` to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use `str(args)` to normalize. We can ignore potential `kwargs` for now.

Execute the wrapped function to retrieve the output. Store the output using `rpush` in the `"...:outputs"` list, then return the output.

Decorate `Cache.store` with `call_history`.<br>
```
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic# cat 3-main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic# ./3-main.py
286e440c-4930-424f-8dc7-fd2820cd29f2
679bf83a-83f2-47f0-849f-0dae02572875
5db34265-efd5-490a-b33a-3b7ff0a4df82
inputs: [b"('first',)", b"('secont',)", b"('third',)"]
outputs: [b'286e440c-4930-424f-8dc7-fd2820cd29f2', b'679bf83a-83f2-47f0-849f-0dae02572875', b'5db34265-efd5-490a-b33a-3b7ff0a4df82']
root@be9c7cae60b5:/alx-backend-storage/0x02-redis_basic#
```

[4. Retrieving lists](./exercise.py)<br>
In this tasks, we will implement a `replay` function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:
```
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```
Tip: use `lrange` and `zip` to loop over inputs and outputs.

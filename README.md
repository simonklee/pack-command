# Redis Packer

A C extension to optimize Redis format in Python.

Potentially it should be merged into Python hiredis bindings
if I make it production ready. Currently I'm just scratching
an itch.

## TODO

- Fix/check for leaks
- Be smarter with allocs.

# Usage

```python
import redis
import redis_packer

class MyConnection(redis.Connection):
    pack_command = redis_packer.pack_command

pool = redis.ConnectionPool(connection_class=MyConnection)

conn = redis.StrictRedis(connection_pool=pool)
```

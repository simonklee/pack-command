[![Build Status](https://travis-ci.org/simonz05/pack-command.png?branch=master)](https://travis-ci.org/simonz05/pack-command)

# Pack Command 

A C extension to optimize Redis format for redis-py.

# Usage

```python
import redis
import pack_command

class MyConnection(redis.Connection):
    pack_command = pack_command.pack_command

pool = redis.ConnectionPool(connection_class=MyConnection)

conn = redis.StrictRedis(connection_pool=pool)
print conn.exists('foo')
```

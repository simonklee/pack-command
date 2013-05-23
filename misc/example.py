import redis
import pack_command

class MyConnection(redis.Connection):
    pack_command = pack_command.pack_command

pool = redis.ConnectionPool(connection_class=MyConnection)

conn = redis.StrictRedis(connection_pool=pool)
print conn.exists('foo')

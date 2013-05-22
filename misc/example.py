import redis
import redis_packer

tests = [
    ("*2\r\n$4\r\nPING\r\n$4\r\nPONG\r\n", ("PING", "PONG")),
    ("*3\r\n$3\r\nSET\r\n$3\r\nfoo\r\n$3\r\nbar\r\n", ("SET", "foo", "bar")),
    ("*2\r\n$3\r\nGET\r\n$3\r\nfoo\r\n", ("GET", "foo")),
    ("*4\r\n$4\r\nZADD\r\n$3\r\nfoo\r\n$4\r\n1000\r\n$3\r\n100\r\n", ("ZADD", "foo", 1000, 100)),
    ("*4\r\n$4\r\nZADD\r\n$3\r\nfoo\r\n$9\r\n136919834\r\n$5\r\n10548\r\n", ("ZADD", "foo", 1369198341, 10548)),
]

for exp, args in tests:
    got = redis_packer.pack_command(*args)
    assert exp == got, "expected %s, got %s" % (exp, got)

class MyConnection(redis.Connection):
    pack_command = redis_packer.pack_command

pool = redis.ConnectionPool(connection_class=MyConnection)

conn = redis.StrictRedis(connection_pool=pool)
print conn.exists('foo')

import pack_command
import unittest

tests = [
    ("*2\r\n$4\r\nPING\r\n$4\r\nPONG\r\n", ("PING", "PONG")),
    ("*3\r\n$3\r\nSET\r\n$3\r\nfoo\r\n$3\r\nbar\r\n", ("SET", "foo", "bar")),
    ("*2\r\n$3\r\nGET\r\n$3\r\nfoo\r\n", ("GET", "foo")),
    ("*4\r\n$4\r\nZADD\r\n$3\r\nfoo\r\n$4\r\n1000\r\n$3\r\n100\r\n", ("ZADD", "foo", 1000, 100)),
    ("*4\r\n$4\r\nZADD\r\n$3\r\nfoo\r\n$10\r\n1369198341\r\n$5\r\n10548\r\n", ("ZADD", "foo", 1369198341, 10548)),
]

class PackCommandTestCase(unittest.TestCase):
    def test_tests(self):
        for exp, args in tests:
            got = pack_command.pack_command(*args)
            self.assertEqual(exp, got)

import unittest
import tempfile
from config import Config


class Case1(unittest.TestCase):
    def setUp(self):
        config1 = b'{"foo": 1.1, "bar": "2.2"}'
        f = tempfile.NamedTemporaryFile()
        f.write(config1)
        f.seek(0)
        self.c1 = Config(f.name)
        self.c2 = Config()

    def test1(self):
        assert self.c1.env == self.c2.env

    def test2(self):
        assert self.c1.env == {"foo": 1.1, "bar": "2.2"}

    def test3(self):
        assert id(self.c1) != id(self.c2)

    def test4(self):
        assert id(self.c1.__dict__) == id(self.c2.__dict__)

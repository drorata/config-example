import unittest
import tempfile
from config import Config


class Case2(unittest.TestCase):
    def setUp(self):
        config1 = b'{"bar": 1.1, "foo": "2.2"}'
        f = tempfile.NamedTemporaryFile()
        f.write(config1)
        f.seek(0)
        self.c1 = Config(f.name)
        self.c2 = Config()

    def test1(self):
        assert self.c1.env == self.c2.env

    def test2(self):
        assert self.c1.env == {"bar": 1.1, "foo": "2.2"}

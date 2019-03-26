from utils import Compression

class Vertex(object):
    def __init__(self, identifier, ctype):
        self.id = identifier
        self.type = ctype

    def compress(self):
        return Compression.compress(self)

    @staticmethod
    def decompress(val):
        return Compression.decompress(val)

    def __repr__(self):
        return '{}-{}'.format(self.id, self.type)


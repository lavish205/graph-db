import cPickle
import zlib


class Compression(object):

    @staticmethod
    def compress(obj):
        compressed = zlib.compress(cPickle.dumps(obj))
        return compressed


    @staticmethod
    def decompress(compressed):
        obj = cPickle.loads(zlib.decompress(compressed))
        return obj


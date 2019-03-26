from utils import Compression


class Edge(object):
    class Direction:
        FORWARD = 0
        REVERSE = 1

    def __init__(self, frm, to, label, direction):
        self.frm = frm
        self.to = to
        self.label = label
        self.direction = direction


    @classmethod
    def decompress(cls, raw_edge):
        edge = Compression.decompress(raw_edge)
        return edge

    def compress(self):
        return Compression.compress(self)


class ForwardEdge(Edge):
    def __init__(self, frm, to, label):
        super(ForwardEdge, self).__init__(frm, to, label, Edge.Direction.FORWARD)


class ReverseEdge(Edge):
    def __init__(self, frm, to, label):
        super(ReverseEdge, self).__init__(frm, to, label,
            Edge.Direction.REVERSE)





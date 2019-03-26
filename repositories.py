from connection import HConnection
from edge import Edge

class IVertexRepository(object):
    def __init__(self):
        pass

class DataWriter(object):
    def __init__(self, column_family):
        self.cf = column_family
        self.val = {}

    def write(self, col, value):
        self.val["{}:{}".format(self.cf, col)] = bytes(value)
        return self

    def get(self):
        return self.val

class HBaseVertexRepository(IVertexRepository):

    def __init__(self):
        self.connection = HConnection("ip").connect()
        self.table = self.connection.table('vertex')

    def create_vertex(self, vertex):
        row_key = self.get_row_key(vertex)
	writer = DataWriter("V")

        (writer
            .write("obj", vertex.compress()))

	self.table.put(row_key, writer.get())

    def get_row_key(self, vertex):
        return b"{}:{}".format(vertex.type, str(vertex.id))


class IEdgeRepository(object):
    def __init__(self):
        pass

class HBaseEdgeRepository(IEdgeRepository):
    def __init__(self):
        self.connection = HConnection("ip").connect()
        self.table = self.connection.table('edge')

    def create_edge(self, edge):
        row_key = self.get_row_key(edge)

        val = (DataWriter("E")
            .write("obj", edge.compress())
            .get())

        self.table.put(row_key, val)

    def get_row_key(self, edge):
        return self.get_frow_key(edge)

    def get_frow_key(self, edge):
        forward_key = b'{}:{}:{}:{}:{}:{}'.format(
            edge.direction, edge.frm.id, edge.frm.type,
            edge.label, edge.to.id, edge.to.type
            )
        return forward_key

    def get_forward_edges(self, frm, label):
        scan_key = b'{}:{}:{}:{}'.format(Edge.Direction.FORWARD,
            frm.id, frm.type, label)


        raw_edges = list(self.table.scan(row_prefix=scan_key))

        edges = [Edge.decompress(edge[1]['E:obj']) for edge in raw_edges]
        return edges

    def get_reverse_edges(self, frm, label):
        scan_key = b'{}:{}:{}:{}'.format(Edge.Direction.REVERSE,
            frm.id, frm.type, label)


        raw_edges = list(self.table.scan(row_prefix=scan_key))

        edges = [Edge.decompress(edge[1]['E:obj']) for edge in raw_edges]
        return edges

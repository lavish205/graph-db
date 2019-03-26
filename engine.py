from repositories import HBaseVertexRepository, HBaseEdgeRepository
from edge import ForwardEdge, ReverseEdge

class GraphEngine(object):
    def __init__(self):
        self.vertex_repo = HBaseVertexRepository()
        self.edge_repo = HBaseEdgeRepository()

    def init(self):
        self.vertex_repo.connect()
        self.edge_repo.connect()


    def connect(self, fro, to, label):
        self.vertex_repo.create_vertex(fro)
        self.vertex_repo.create_vertex(to)

        edge = ForwardEdge(fro, to, label)
        redge = ReverseEdge(to, fro, label)

        self.edge_repo.create_edge(edge)
        self.edge_repo.create_edge(redge)


    def fanout(self, frm, label):
        edges = self.edge_repo.get_forward_edges(frm, label)
        return [edge.to for edge in edges]

    def fanin(self, frm, label):
        edges = self.edge_repo.get_reverse_edges(frm, label)
        return [edge.to for edge in edges]




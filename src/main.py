from vertex import Vertex
from engine import GraphEngine


class NodeType:
    ADMIN = 'ADMIN'
    TEST = 'TEST'

class EdgeLabel:
    CREATED = 'CREATED'


def start():
    g = GraphEngine()
    fro = Vertex(1, NodeType.ADMIN)
    to = Vertex(2, NodeType.TEST)

    tos = [Vertex(i, NodeType.TEST) for i in range(5)]

    for ti in tos:
        g.connect(fro, ti, EdgeLabel.CREATED)

    print g.fanout(fro, EdgeLabel.CREATED)
    print g.fanin(tos[0], EdgeLabel.CREATED)
    print g.fanin(fro, EdgeLabel.CREATED)


if __name__ == '__main__':
    start()

from GraphML.GraphML import GraphML
from GraphML.formatter.XMLFormatter import XMLFormatter
from GraphML.graph.Graph import Graph
from GraphML.graph.elements.data.Data import Data
from GraphML.graph.elements.edge.Edge import Edge
from GraphML.graph.elements.key.Key import Key
from GraphML.graph.elements.node.Node import Node

if __name__ == "__main__":
    graphml = GraphML()
    node1 = Node().add_data(Data(key=Key(), pcdata="value"))
    node2 = Node().add_data(Data(key=Key(), pcdata="value2"))
    graphml.add_graph(
        Graph()
        .add_nodes([node1, node2])
        .add_edge(Edge(source=node1.node_id, target=node2.node_id))
    )

    print(XMLFormatter.format(graphml.to_xml()))

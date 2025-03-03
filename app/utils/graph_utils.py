import networkx as nx


def build_graph(graph_data):
    graph = nx.DiGraph()
    for entry in graph_data:
        graph.add_edge(
            entry["source"],
            entry["destination"],
            method=entry["method"],
            type=entry["type"],
            calls=entry["calls"],
            avg_duration=entry["avg_duration"]
        )
    return graph


def detect_cyclic_dependencies(graph):
    return list(nx.simple_cycles(graph))


def detect_bottlenecks(graph):
    return [node for node, degree in graph.in_degree() if degree > 5]


def detect_high_fan_out(graph):
    return [node for node, degree in graph.out_degree() if degree > 5]

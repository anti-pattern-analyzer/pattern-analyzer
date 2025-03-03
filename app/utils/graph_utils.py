import networkx as nx


def build_graph(graph_data):
    graph = nx.DiGraph()

    for entry in graph_data:
        graph.add_edge(
            entry["source"],
            entry["destination"],
            method=entry["method"],
            type=entry["type"],  # GET, POST, PATCH, PUT, EVENT
            calls=entry["calls"],
            avg_duration=entry["avg_duration"]
        )

    return graph


def detect_cyclic_dependencies(graph):
    """Find cyclic dependencies using strongly connected components (SCC)."""
    return list(nx.simple_cycles(graph))


def detect_the_knot(graph):
    """Detect dense clusters of interrelated services."""
    clustering_coefficients = nx.clustering(graph)
    return [node for node, coeff in clustering_coefficients.items() if coeff > 0.7]  # Adjust threshold as needed


def detect_bottlenecks(graph):
    """Detect services that receive a high number of incoming calls."""
    return [node for node, degree in graph.in_degree() if degree > 5]  # Threshold for bottleneck detection


def detect_nano_services(graph):
    """Detect services with very few dependencies."""
    return [node for node, degree in graph.degree() if degree <= 2]


def detect_long_chains(graph, threshold=5):
    """Find excessively long service chains (path length > threshold)."""
    long_chains = []
    for node in graph.nodes:
        for target in graph.nodes:
            if node != target:
                try:
                    length = nx.shortest_path_length(graph, source=node, target=target)
                    if length > threshold:
                        long_chains.append({"source": node, "target": target, "length": length})
                except nx.NetworkXNoPath:
                    pass
    return long_chains


def detect_fan_in_overload(graph, threshold=5):
    """Detect services that receive calls from too many upstream services."""
    return [node for node, degree in graph.in_degree() if degree > threshold]


def detect_fan_out_overload(graph, threshold=5):
    """Detect services that call too many downstream services."""
    return [node for node, degree in graph.out_degree() if degree > threshold]


def detect_chatty_services(graph, threshold=10):
    """Detect services making excessive direct interactions per request."""
    return [node for node, degree in graph.degree() if degree > threshold]


def detect_sync_overuse(graph, time_threshold=500):
    """Detect excessive synchronous (blocking) calls causing performance issues."""
    return [
        edge for edge in graph.edges(data=True)
        if edge[2]["type"] in ("GET", "POST", "PATCH", "PUT") and edge[2]["avg_duration"] > time_threshold
    ]


def detect_improper_api_gateway_usage(graph):
    """Detect APIs that handle too much execution time (API Gateway bottlenecks)."""
    return [
        edge for edge in graph.edges(data=True)
        if "gateway" in edge[0].lower() and edge[2]["avg_duration"] > 1000
    ]


def detect_eventual_consistency_pitfalls(graph, delay_threshold=2000):
    """Detect event-based async calls with high latency (potential inconsistency issues)."""
    return [
        edge for edge in graph.edges(data=True)
        if edge[2]["type"] == "EVENT" and edge[2]["avg_duration"] > delay_threshold
    ]


def detect_improper_load_balancer(graph):
    """Detect uneven request distribution (some services overloaded while others are idle)."""
    avg_requests = sum(dict(graph.degree()).values()) / len(graph.nodes)
    return [
        node for node, degree in graph.degree()
        if degree > avg_requests * 1.5 or degree < avg_requests * 0.5  # Imbalance detection
    ]

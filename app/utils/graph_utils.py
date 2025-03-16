import networkx as nx


def build_graph(graph_data):
    graph = nx.DiGraph()
    for entry in graph_data:
        graph.add_edge(
            entry["source"],
            entry["target"],
            method=entry.get("method", "UNKNOWN"),
            type=entry.get("type", "UNKNOWN"),
            calls=entry.get("calls", 1),
            avg_duration=entry.get("avg_duration", 0)
        )
    return graph


def detect_cyclic_dependencies(graph):
    cycles = [
        {"cycle": list(cycle), "cycle_length": len(cycle)}
        for cycle in {tuple(sorted(cycle)) for cycle in nx.simple_cycles(graph)}
    ]
    return cycles


def detect_the_knot(graph, threshold=0.7):
    clustering_coefficients = nx.clustering(graph)
    return [
        {"service": node, "coefficient": coeff}
        for node, coeff in clustering_coefficients.items() if coeff > threshold
    ]


def detect_bottlenecks(graph, threshold=5):
    return [
        {"service": node, "incoming_calls": degree}
        for node, degree in graph.in_degree() if degree > threshold
    ]


def detect_nano_services(graph, threshold=2):
    return [
        {"service": node, "total_connections": degree}
        for node, degree in graph.degree() if degree <= threshold
    ]


def detect_long_chains(graph, threshold=5):
    long_chains = set()
    for node in graph.nodes:
        for target in graph.nodes:
            if node != target:
                try:
                    length = nx.shortest_path_length(graph, source=node, target=target)
                    if length > threshold:
                        long_chains.add((min(node, target), max(node, target), length))
                except nx.NetworkXNoPath:
                    pass
    return [{"source": chain[0], "target": chain[1], "length": chain[2]} for chain in long_chains]


def detect_fan_in_overload(graph, threshold=2):
    fan_in_nodes = {}
    for node in graph.nodes:
        upstream_services = list(graph.predecessors(node))
        if len(upstream_services) > threshold:
            fan_in_nodes[node] = {
                "upstream_services": upstream_services,
                "total_upstream": len(upstream_services)
            }
    return fan_in_nodes


def detect_fan_out_overload(graph, threshold=3):
    fan_out_nodes = {}
    for node in graph.nodes:
        downstream_services = set(graph.successors(node))
        if len(downstream_services) > threshold:
            fan_out_nodes[node] = {
                "downstream_services": list(downstream_services),
                "total_downstream": len(downstream_services)
            }
    return fan_out_nodes


def detect_chatty_services(graph):
    all_calls = [
        sum(graph.get_edge_data(node, target).get("calls", 0) for target in graph.successors(node))
        for node in graph.nodes
    ]

    if not all_calls:
        return []

    avg_calls = sum(all_calls) / len(all_calls)
    threshold = avg_calls * 1.5

    chatty_nodes = {
        node: {
            "total_calls": sum(graph.get_edge_data(node, target).get("calls", 0) for target in graph.successors(node)),
            "avg_duration": sum(graph.get_edge_data(node, target).get("avg_duration", 0) for target in
                                list(graph.successors(node))) / max(len(list(graph.successors(node))), 1),
            "connected_services": list(graph.successors(node))
        }
        for node in graph.nodes
        if (total_calls := sum(
            graph.get_edge_data(node, target).get("calls", 0) for target in graph.successors(node))) > threshold
    }

    return chatty_nodes


def detect_sync_overuse(graph, time_threshold=500):
    return [
        {
            "source": edge[0],
            "destination": edge[1],
            "method": edge[2]["method"],
            "avg_duration": edge[2]["avg_duration"],
            "call_type": edge[2]["type"]
        }
        for edge in graph.edges(data=True)
        if edge[2]["type"] in ("GET", "POST", "PATCH", "PUT") and edge[2]["avg_duration"] > time_threshold
    ]


def detect_improper_api_gateway_usage(graph):
    return [
        {
            "api_gateway": edge[0],
            "service": edge[1],
            "avg_duration": edge[2]["avg_duration"]
        }
        for edge in graph.edges(data=True)
        if "gateway" in edge[0].lower() and edge[2]["avg_duration"] > 1000
    ]


def detect_eventual_consistency_pitfalls(graph, delay_threshold=2000):
    return [
        {
            "source": edge[0],
            "destination": edge[1],
            "method": edge[2]["method"],
            "avg_duration": edge[2]["avg_duration"]
        }
        for edge in graph.edges(data=True)
        if edge[2]["type"] == "EVENT" and edge[2]["avg_duration"] > delay_threshold
    ]


def detect_improper_load_balancer(graph):
    degrees = dict(graph.degree())
    avg_requests = sum(degrees.values()) / len(graph.nodes)

    return [
        {
            "service": node,
            "requests": degree,
            "imbalance_factor": round(degree / avg_requests, 2)
        }
        for node, degree in degrees.items()
        if degree > avg_requests * 1.5 or degree < avg_requests * 0.5
    ]

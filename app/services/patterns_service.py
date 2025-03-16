from app.repositories.graph_repository import fetch_graph_data
from app.utils.graph_utils import (
    build_graph, detect_cyclic_dependencies, detect_the_knot, detect_bottlenecks,
    detect_nano_services, detect_long_chains, detect_fan_in_overload,
    detect_fan_out_overload, detect_chatty_services, detect_sync_overuse,
    detect_improper_api_gateway_usage, detect_eventual_consistency_pitfalls,
    detect_improper_load_balancer
)


def detect_cyclic_anti_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    cycles = detect_cyclic_dependencies(graph)
    return {"anti_pattern": "Cyclic Dependency", "cycles": cycles}


def detect_knot_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    dense_clusters = detect_the_knot(graph)
    return {"anti_pattern": "The Knot", "dense_clusters": dense_clusters}


def detect_bottleneck_anti_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    bottlenecks = detect_bottlenecks(graph)
    return {"anti_pattern": "Bottleneck Services", "services": bottlenecks}


def detect_nano_service_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    nano_services = detect_nano_services(graph)
    return {"anti_pattern": "Nano Services", "services": nano_services}


def detect_long_chain_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    long_chains = detect_long_chains(graph)
    return {"anti_pattern": "Long Service Chains", "chains": long_chains}


def detect_fan_in_overload_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    overloads = detect_fan_in_overload(graph)
    return {"anti_pattern": "Service Fan-in Overload", "services": overloads}


def detect_fan_out_overload_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    overloads = detect_fan_out_overload(graph)
    return {"anti_pattern": "Service Fan-out Overload", "services": overloads}


def detect_chatty_service_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    chatty_services = detect_chatty_services(graph)
    return {"anti_pattern": "Chatty Services", "services": chatty_services}


def detect_sync_overuse_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    sync_issues = detect_sync_overuse(graph)
    return {"anti_pattern": "Synchronous Call Overuse", "issues": sync_issues}


def detect_improper_api_gateway_usage_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    gateway_issues = detect_improper_api_gateway_usage(graph)
    return {"anti_pattern": "Improper API Gateway Usage", "issues": gateway_issues}


def detect_eventual_consistency_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    consistency_issues = detect_eventual_consistency_pitfalls(graph)
    return {"anti_pattern": "Eventual Consistency Pitfall", "issues": consistency_issues}


def detect_improper_load_balancer_patterns():
    graph_data = fetch_graph_data()
    graph = build_graph(graph_data["links"])
    imbalance_issues = detect_improper_load_balancer(graph)
    return {"anti_pattern": "Improper Load Balancer", "imbalances": imbalance_issues}

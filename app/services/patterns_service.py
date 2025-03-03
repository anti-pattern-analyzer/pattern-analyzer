from app.repositories.graph_repository import fetch_graph_data
from app.utils.graph_utils import build_graph, detect_cyclic_dependencies, detect_bottlenecks, detect_high_fan_out


def detect_cyclic_anti_patterns():
    service_graph = fetch_graph_data()
    graph = build_graph(service_graph)
    cycles = detect_cyclic_dependencies(graph)
    return {"anti_pattern": "Cyclic Dependency", "cycles": cycles}


def detect_bottleneck_anti_patterns():
    service_graph = fetch_graph_data()
    graph = build_graph(service_graph)
    bottlenecks = detect_bottlenecks(graph)
    return {"anti_pattern": "Bottleneck Services", "services": bottlenecks}


def detect_high_fan_out_patterns():
    service_graph = fetch_graph_data()
    graph = build_graph(service_graph)
    high_fan_out_services = detect_high_fan_out(graph)
    return {"anti_pattern": "High Fan-Out", "services": high_fan_out_services}

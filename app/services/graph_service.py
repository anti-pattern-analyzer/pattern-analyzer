from app.repositories.graph_repository import fetch_graph_data


def get_graph_data():
    service_graph = fetch_graph_data()
    return service_graph

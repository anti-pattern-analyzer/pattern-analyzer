from app.repositories.graph_repository import fetch_graph_data


def get_graph_data():
    """Retrieve the full system graph with detailed interaction data."""
    return fetch_graph_data()

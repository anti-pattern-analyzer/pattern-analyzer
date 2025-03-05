from app.repositories.graph_repository import fetch_graph_data, fetch_graph_summary


def get_graph_data():
    """Retrieve the full system graph with detailed interaction data."""
    return fetch_graph_data()


def get_graph_summary():
    """Retrieve a high-level summary of the system for visualization."""
    return fetch_graph_summary()

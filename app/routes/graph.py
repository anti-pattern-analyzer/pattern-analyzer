from fastapi import APIRouter
from app.services.graph_service import get_graph_data, get_graph_summary

router = APIRouter()


@router.get("/")
async def fetch_graph():
    """Fetch full system graph with service interactions."""
    graph = get_graph_data()
    return {"status": "success", "graph": graph}


@router.get("/summary")
async def fetch_graph_summary():
    """Fetch high-level summary for React-D3 graph visualization."""
    summary = get_graph_summary()
    return {"status": "success", "graph": summary}

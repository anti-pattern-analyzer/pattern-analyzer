from fastapi import APIRouter
from app.services.graph_service import get_graph_data

router = APIRouter()


@router.get("/")
async def fetch_graph():
    """Fetch full system graph with service interactions."""
    graph = get_graph_data()
    return {"status": "success", "graph": graph}

from fastapi import APIRouter

from app.services.graph_service import get_graph_data

router = APIRouter()


@router.get("/")
async def fetch_graph():
    graph = get_graph_data()
    return {"status": "success", "graph": graph}

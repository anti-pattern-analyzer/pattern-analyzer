from fastapi import APIRouter

from .graph import router as graph_router
from .patterns import router as patterns_router

router = APIRouter()

router.include_router(patterns_router, prefix="/patterns", tags=["Anti-Patterns"])
router.include_router(graph_router, prefix="/graph", tags=["Graph Queries"])

from fastapi import APIRouter

from app.services.patterns_service import detect_cyclic_anti_patterns, detect_bottleneck_anti_patterns

router = APIRouter()


@router.get("/patterns/cycles")
def get_cyclic_dependencies():
    return detect_cyclic_anti_patterns()


@router.get("/patterns/bottlenecks")
def get_bottleneck_services():
    return detect_bottleneck_anti_patterns()

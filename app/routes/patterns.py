from fastapi import APIRouter

from app.services.patterns_service import detect_cyclic_anti_patterns, detect_bottleneck_anti_patterns, \
    detect_high_fan_out_patterns

router = APIRouter()


@router.get("/cyclic")
async def get_cyclic_dependencies():
    return detect_cyclic_anti_patterns()


@router.get("/bottleneck")
async def get_bottleneck_services():
    return detect_bottleneck_anti_patterns()


@router.get("/high-fan-out")
async def get_high_fan_out_services():
    return detect_high_fan_out_patterns()

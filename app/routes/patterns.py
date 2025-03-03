from fastapi import APIRouter

from app.services.patterns_service import (
    detect_cyclic_anti_patterns, detect_knot_patterns, detect_bottleneck_anti_patterns,
    detect_nano_service_patterns, detect_long_chain_patterns, detect_fan_in_overload_patterns,
    detect_fan_out_overload_patterns, detect_chatty_service_patterns, detect_sync_overuse_patterns,
    detect_improper_api_gateway_usage_patterns, detect_eventual_consistency_patterns,
    detect_improper_load_balancer_patterns
)

router = APIRouter()


@router.get("/cyclic")
async def get_cyclic_dependencies():
    return detect_cyclic_anti_patterns()


@router.get("/knot")
async def get_knot_patterns():
    return detect_knot_patterns()


@router.get("/bottleneck")
async def get_bottleneck_services():
    return detect_bottleneck_anti_patterns()


@router.get("/nano-services")
async def get_nano_services():
    return detect_nano_service_patterns()


@router.get("/long-chain")
async def get_long_service_chains():
    return detect_long_chain_patterns()


@router.get("/fan-in")
async def get_fan_in_overload():
    return detect_fan_in_overload_patterns()


@router.get("/fan-out")
async def get_fan_out_overload():
    return detect_fan_out_overload_patterns()


@router.get("/chatty")
async def get_chatty_services():
    return detect_chatty_service_patterns()


@router.get("/sync-overuse")
async def get_sync_overuse():
    return detect_sync_overuse_patterns()


@router.get("/api-gateway")
async def get_api_gateway_usage():
    return detect_improper_api_gateway_usage_patterns()


@router.get("/consistency")
async def get_eventual_consistency():
    return detect_eventual_consistency_patterns()


@router.get("/load-balancer")
async def get_improper_load_balancer():
    return detect_improper_load_balancer_patterns()

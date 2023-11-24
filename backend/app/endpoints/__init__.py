from .ping import api_router as router_health
from .auth import api_router as router_auth


list_of_routes = [
    router_health,
    router_auth
]


__all__ = [
    "list_of_routes"
]

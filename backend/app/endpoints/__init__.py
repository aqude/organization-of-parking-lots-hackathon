from .ping import api_router as router_health
from .auth import api_router as router_auth
from .get_places import api_router as router_places
from .update_place import api_router as update_router
from .reservation import api_router as reservation_router
from .review import router as review_router


list_of_routes = [
    router_health,
    router_auth,
    router_places,
    update_router,
    reservation_router,
    review_router,
]


__all__ = ["list_of_routes"]
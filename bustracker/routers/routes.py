from uuid import UUID

from bustracker.core import Route, RouteStop
from bustracker.core.services import RouteService, RouteStopService
from bustracker.database import get_session
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/routes")
routes_router = APIRouter(tags=["routes"])
stops_router = APIRouter(prefix="/{route_id}/stops", tags=["route_stops"])


@routes_router.get("/", response_model=list[Route])
def read_routes(db: Session = Depends(get_session)):
    return RouteService(db).list()


@routes_router.put("/", response_model=Route, responses={409: {}})
def create_or_update_route(route: Route, db: Session = Depends(get_session)):
    return RouteService(db).update(route)


@routes_router.get("/{route_id}", response_model=Route, responses={404: {}})
def read_route(route_id: UUID, db: Session = Depends(get_session)):
    return RouteService(db).get(route_id)


@routes_router.delete("/{route_id}", responses={409: {}})
def delete_route(route_id: UUID, db: Session = Depends(get_session)):
    return RouteService(db).delete(route_id)


@stops_router.get("/", response_model=list[RouteStop])
def read_route_stops(route_id: UUID, db: Session = Depends(get_session)):
    return RouteStopService(db).list(route_id=route_id)


@stops_router.put("/{stop_id}", response_model=RouteStop, responses={409: {}})
def create_route_stop(
    route_id: UUID,
    stop_id: UUID,
    db: Session = Depends(get_session),
):
    return RouteStopService(db).create(route_id=route_id, stop_id=stop_id)


@stops_router.get("/{stop_id}", response_model=RouteStop, responses={404: {}})
def read_route_stop(
    route_id: UUID,
    stop_id: UUID,
    db: Session = Depends(get_session),
):
    return RouteStopService(db).get(route_id=route_id, stop_id=stop_id)


@stops_router.delete("/{stop_id}", responses={409: {}})
def delete_route_stop(
    route_id: UUID,
    stop_id: UUID,
    db: Session = Depends(get_session),
):
    return RouteStopService(db).delete(route_id=route_id, stop_id=stop_id)


router.include_router(routes_router)
router.include_router(stops_router)

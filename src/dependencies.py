from typing import Annotated

from fastapi import Depends

from src.infrastructure.db import SessionFactory
from src.infrastructure.unit_of_work import UnitOfWork
from src.maintenance.mapper import MaintenanceMapper
from src.maintenance.repo import MaintenanceRepo
from src.maintenance.service import MaintenanceService


async def get_maintenance_service_read() -> MaintenanceService:
    unit_of_work = UnitOfWork(SessionFactory, read_only=True)
    maintenance_repo = MaintenanceRepo
    maintenance_mapper = MaintenanceMapper()
    return MaintenanceService(unit_of_work, maintenance_repo, maintenance_mapper)

async def get_maintenance_service_write() -> MaintenanceService:
    unit_of_work = UnitOfWork(SessionFactory)
    maintenance_repo = MaintenanceRepo
    maintenance_mapper = MaintenanceMapper()
    return MaintenanceService(unit_of_work, maintenance_repo, maintenance_mapper)


MaintenanceServiceReadDep = Annotated[MaintenanceService, Depends(get_maintenance_service_read)]
MaintenanceServiceWriteDep = Annotated[MaintenanceService, Depends(get_maintenance_service_write)]
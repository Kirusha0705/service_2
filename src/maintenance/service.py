from uuid import UUID

from sqlalchemy.util import await_

from src.infrastructure.unit_of_work import UnitOfWork
from src.maintenance.repo import MaintenanceRepo
from src.maintenance.schema import MaintenanceResponse, MaintenanceCreate


class MaintenanceService:

    def __init__(
            self,
            unit_of_work: UnitOfWork,
            maintenance_repo: type[MaintenanceRepo]
    ) -> None:

        self.unit_of_work = unit_of_work
        self.maintenance_repo = maintenance_repo


    async def read_maintenance(
            self,
            car_id: UUID
    ) -> MaintenanceResponse:
        return ''

    async def create_maintenance(
            self,
            maintenance_data: MaintenanceCreate
    ) -> MaintenanceResponse:
        return ''

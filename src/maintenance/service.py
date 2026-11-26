from uuid import UUID

from sqlalchemy.util import await_

from src.infrastructure import unit_of_work
from src.infrastructure.unit_of_work import UnitOfWork
from src.maintenance.exceptions import ObjectNotFoundException
from src.maintenance.mapper import MaintenanceMapper
from src.maintenance.repo import MaintenanceRepo
from src.maintenance.schema import MaintenanceResponse, MaintenanceCreate


class MaintenanceService:

    def __init__(
            self,
            unit_of_work: UnitOfWork,
            maintenance_repo: type[MaintenanceRepo],
            maintenance_mapper: MaintenanceMapper
    ) -> None:

        self.unit_of_work = unit_of_work
        self.maintenance_repo = maintenance_repo
        self.maintenance_mapper = maintenance_mapper


    async def read_maintenance(
            self,
            car_id: UUID
    ) -> MaintenanceResponse:
        async with self.unit_of_work:
            maintenance_model =  await self._read_entity_or_exception(car_id=car_id)
            maintenance_schema = self.maintenance_mapper.map_model_to_schema(maintenance_model)
        return maintenance_schema


    async def create_maintenance(
            self,
            maintenance_data: MaintenanceCreate
    ) -> MaintenanceResponse:
        maintenance_model = self.maintenance_mapper.map_shema_to_model(maintenance_data)
        async with self.unit_of_work as uow:
            maintenance_repo = self.maintenance_repo(uow.session)
            await maintenance_repo.create(maintenance_model)
            maintenance_schema = self.maintenance_mapper.map_model_to_schema(maintenance_model)
        return maintenance_schema

    async def _read_entity_or_exception(self, car_id: UUID):
        maintenance_repo = self.maintenance_repo(self.unit_of_work.session)
        maintenance_model = await maintenance_repo.read_one_or_none(car_id=car_id)

        if maintenance_model is None:
            raise ObjectNotFoundException('Data about maintenance was not found')

        return maintenance_model
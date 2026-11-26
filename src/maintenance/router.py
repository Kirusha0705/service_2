from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Path
from starlette import status

from src.dependencies import MaintenanceServiceReadDep
from src.maintenance.schema import MaintenanceCreate, MaintenanceResponse

router = APIRouter(prefix='/maintenance', tags=['Техническое обслуживание'])


@router.get('/{car_id}', response_model=MaintenanceResponse)
async def read_maintenance(
        maintenance_service: MaintenanceServiceReadDep,
        car_id: UUID = Path(description='ID машины')
):
    return maintenance_service.read_maintenance(car_id)

@router.post('/{car_id}', response_model=MaintenanceResponse, status_code=status.HTTP_201_CREATED)
async def create_maintenance(
        maintenance_data: MaintenanceCreate,
        maintenance_service: MaintenanceServiceReadDep,
):
    return maintenance_service.create_maintenance(maintenance_data)

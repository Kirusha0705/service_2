from src.maintenance.model import MaintenanceModel
from src.maintenance.schema import MaintenanceResponse, MaintenanceCreate


class MaintenanceMapper:

    @staticmethod
    def map_model_to_schema(maintenance_model: MaintenanceModel) -> MaintenanceResponse:
        return MaintenanceResponse.model_validate(maintenance_model)

    @staticmethod
    def map_shema_to_model(maintenance_data: MaintenanceCreate) -> MaintenanceModel:
        maintenance_data = maintenance_data.model_dump()
        return MaintenanceModel(**maintenance_data)
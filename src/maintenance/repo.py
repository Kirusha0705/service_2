from src.infrastructure.base_repo import BaseRepository
from src.maintenance.model import MaintenanceModel


class MaintenancesRepo(BaseRepository):
    model = MaintenanceModel
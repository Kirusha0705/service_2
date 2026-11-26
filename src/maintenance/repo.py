from src.infrastructure.base_repo import BaseRepository
from src.maintenance.model import MaintenanceModel


class MaintenanceRepo(BaseRepository):
    model = MaintenanceModel
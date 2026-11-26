from datetime import date
from uuid import UUID

from pydantic import BaseModel, model_validator


class MaintenanceCreate(BaseModel):
    car_id: UUID
    last_date_maintenance: date
    next_date_maintenance: date

    @model_validator(mode='after')
    def check_date(self):
        if self.last_date_maintenance >= self.next_date_maintenance:
            raise ValueError('Date of last maintenance cannot be greater than next maintenance')
        return self

class MaintenanceResponse(BaseModel):
    car_id: UUID
    last_date_maintenance: date
    next_date_maintenance: date




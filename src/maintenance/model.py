from datetime import date
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Date, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, Composite

from src.infrastructure.base_model import Base


class MaintenanceModel(Base):
    __tablename__ = 'maintenance'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    car_id: Mapped[UUID] = mapped_column(nullable=False)
    last_date_maintenance: Mapped[date] = mapped_column(Date, nullable=False)
    next_date_maintenance: Mapped[date] = mapped_column(Date, nullable=False)

    __table_args__ = (
        CheckConstraint(
            'next_date_maintenance > last_date_maintenance'
        ),
        UniqueConstraint(
            "car_id",
            "last_date_maintenance",
            "next_date_maintenance",
            name="uq_car_data_last_and_next_maintenance",
        ),

    )

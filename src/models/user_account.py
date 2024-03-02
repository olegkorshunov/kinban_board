from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models.kanban_board import KanbanBoard


class UserAccount(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    kanban_board: Mapped["KanbanBoard"] = relationship(back_populates="user_account")

    def __repr__(self) -> str:
        return f"{self.email}"

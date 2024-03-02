from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models.user_account import UserAccount


class KanbanBoard(Base):
    """
    <?xml version="1.0" ?>
    <sections id="sections">
        <section name="in progress">
            <marks>
                <mark1 name="" description="" comment="" deadlione="" />
                ...
            </marks>
        </section>
        ...
    <sections>

    """

    __tablename__ = "kanban_board"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    xml: Mapped[str] = mapped_column(String, nullable=False)
    user_account: Mapped["UserAccount"] = relationship(back_populates="kanban_board")

    def __repr__(self) -> str:
        return f"{self.id}"

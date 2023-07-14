from sqlmodel import SQLModel, Field, DateTime, Column
from typing import Optional
from datetime import datetime

class Query(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    query: str = Field(default=None, nullable=False)
    sales_objection: str = Field(default = None, nullable=True)
    response: str = Field(default=None, nullable=True)
    created_on: datetime = Field(default_factory=datetime.utcnow)
    modified_on: Optional[datetime] = Field(
        sa_column=Column(
            "modified_on",
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        )
    )
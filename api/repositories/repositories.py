from ..dao import db_model
from ..dto import request_model
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.future import select
from typing import Optional

async def get_all_queries(
        session: AsyncSession
):
    query = select(db_model.Query)
    execute_query = await session.execute(query)
    response = execute_query.scalars().all()
    return response

async def create_query(
    session: AsyncSession,
    user_query: request_model.CreateQuery
):
    new_query = db_model.Query.from_orm(user_query)
    session.add(new_query)
    await session.commit()
    await session.refresh(new_query)
    return new_query

async def get_query_by_id(
        id: int,
        session: AsyncSession
):
    query = select(db_model.Query).where(id = id)
    execute_query = await session.execute(query)
    response = execute_query.scalars().first()
    return response

async def delete_query(
        session: AsyncSession, query_obj: db_model.Query
):
    session.delete(query_obj)
    await session.commit()
    return query_obj




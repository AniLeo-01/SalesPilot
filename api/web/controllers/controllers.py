from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_session
from ..dto.request_model import CreateQuery, CreateUserData
from ..services import services

router = APIRouter()

@router.post('/query')
async def get_response_from_query(user_data: CreateUserData, input_data: CreateQuery, session: AsyncSession = Depends(get_session)):
    response = await services.get_response(user_data=user_data ,query_data=input_data, session = session)
    if response:
        return response
    else:
        return "AI failed to provide recommendations for your sales objection"

@router.get('/query')
async def get_all_queries_responses(session: AsyncSession = Depends(get_session)):
    queries = await services.get_all_queries(session = session)
    return queries

@router.delete('/query/{id}')
async def delete_query_history(id: int, session: AsyncSession = Depends(get_session)):
    deleted_query = await services.delete_query_by_id(id = id, session = session)
    return deleted_query


# server/api/v1/endpoints/games.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.concurrency import run_in_threadpool
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from services.price_scraper import GamePriceService
from schemas import GameSchema, GameCreateSchema

router = APIRouter(prefix="/games", tags=["games"])

@router.get("/", response_model=list[GameSchema])
async def get_games(
    db: AsyncSession = Depends(get_db),
    limit: int = 100,
    offset: int = 0
):
    """Получение списка игр с пагинацией"""
    return await GamePriceService.get_games(db, limit=limit, offset=offset)

@router.get("/{game_id}", response_model=GameSchema)
async def get_game_details(
    game_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Получение детальной информации об игре"""
    game = await GamePriceService.get_game_by_id(db, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Игра не найдена")
    return game

@router.post("/compare_prices")
async def compare_prices(
    game_data: GameCreateSchema,
    db: AsyncSession = Depends(get_db)
):
    """Сравнение цен в разных магазинах"""
    # Используем ThreadPool для CPU-bound операций
    result = await run_in_threadpool(
        GamePriceService.compare_prices,
        db,
        game_data
    )
    return {"status": "success", "data": result}
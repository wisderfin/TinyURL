from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from app.backend.components.redirect.utils import get_link_by_short
from app.backend.base.database import get_async_session


router = APIRouter()


@router.get("/{short}")
async def main(short: str, request: Request, session: AsyncSession = Depends(get_async_session)):
    # Небольшое пояснение:
    #   Нельзя одновременно вернуть и перенаправление и result.
    #   Если выбирать result, то не сработает перенаправление.
    #   Если выбирать перенаправление, то Swager от FastAPI будет выдавть ошибку.
    #   Поэтому я разделил запрос по заголовку accept:
    #      1. Если accept равен "application/json" - запрос отправлен из Swager и мы возвращаем result
    #      2. Eсли заголовок другой - запрос отправлен из браузера и возвращаем перенаправление
    accept_header = request.headers.get("accept")
    result = await get_link_by_short(short, session)
    if result is not None:
        if accept_header == "application/json":
            return result
        return RedirectResponse(url=result.full)
    return None

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.components.compressor.schemes import AddLinkScheme
from app.components.compressor.utils import add_link, get_latest_url
from app.components.compressor.services import next_short
from app.base.database import get_async_session
router = APIRouter(prefix="/compressor")


@router.post("/")
async def add(link: AddLinkScheme, session: AsyncSession = Depends(get_async_session)):
    latest_note = await get_latest_url(session)
    short = next_short(latest_note.short)
    next_id = latest_note.id + 1
    result = await add_link(full=link.full, short=short, next_id=next_id, session=session)
    return result



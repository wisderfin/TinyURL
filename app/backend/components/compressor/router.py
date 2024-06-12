from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.backend.components.compressor.schemes import AddLinkScheme
from app.backend.components.compressor.utils import add_link, get_latest_url
from app.backend.components.compressor.services import next_short
from app.backend.base.database import get_async_session
router = APIRouter(prefix="/compressor")


@router.post("/add")
async def add(link: AddLinkScheme, session: AsyncSession = Depends(get_async_session)):
    latest_note = await get_latest_url(session)
    if latest_note is None:
        short = 'AAAAAAAA'
        next_id = 1
    else:
        short = next_short(latest_note.short)
        next_id = latest_note.id + 1
    result = await add_link(full=link.full, short=short, next_id=next_id, session=session)
    return result



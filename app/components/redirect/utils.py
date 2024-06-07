from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.components.compressor.models import LinkModel
from app.components.compressor.schemes import LinkScheme


async def get_link_by_short(short_link: str, session: AsyncSession) -> LinkScheme | None:
    query = select(LinkModel).filter_by(short=short_link)
    result = await session.execute(query)
    link = result.scalars().first()
    if link is not None:
        return LinkScheme(**link.__dict__)
    return None


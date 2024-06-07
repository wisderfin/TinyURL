from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import AnyHttpUrl
from app.components.compressor.models import LinkModel
from app.components.compressor.schemes import LinkScheme


# добавление ссылки в бд
async def add_link(short: str, full: AnyHttpUrl, next_id: int, session: AsyncSession):
    new_link = LinkModel(id=next_id, full=str(full), short=short)
    session.add(new_link)
    await session.commit()
    return new_link.__dict__


async def get_latest_url(session: AsyncSession) -> LinkScheme:
    latest = select(LinkModel).order_by(desc(LinkModel.id))
    latest = await session.execute(latest)
    latest = latest.scalars().first()
    latest_dict = dict(latest.__dict__)
    latest_dict.pop('full', AnyHttpUrl(latest_dict['full']))
    # latest_dict.pop('_sa_instance_state', None)
    return LinkScheme(**latest_dict)

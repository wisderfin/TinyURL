from datetime import datetime
from pydantic import BaseModel, AnyHttpUrl, field_validator


class AddLinkScheme(BaseModel):
    full: AnyHttpUrl

    @field_validator('full')
    def add_protocol(cls, v):
        v = str(v)
        if 'http://' not in v and 'https://' not in v:
            v = f'https://{v}'
        return AnyHttpUrl(v)


class LinkScheme(BaseModel):
    id: int
    short: str
    full: AnyHttpUrl
    created_at: datetime

    @field_validator('full')
    def add_protocol(cls, v):
        v = str(v)
        if 'http://' not in v and 'https://' not in v:
            v = f'https://{v}'
        return AnyHttpUrl(v)

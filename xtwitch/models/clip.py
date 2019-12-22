from __future__ import annotations

from xtwitch.models import attr
from xtwitch.models.base import Model
from xtwitch.models.manager import Manager


class ClipManager(Manager):

    async def get_clip(self, slug: str):
        result = await self._get(f'clips/{slug}')
        return Clip.from_json(result.json())


class Clip(Model):

    class Broadcaster(attr.S):
        id: int
        name: str
        display_name: str
        channel_url: str
        logo: str

    class Curator(attr.S):
        id: int
        name: str
        display_name: str
        channel_url: str
        logo: str

    class Vod(attr.S):
        id: str
        url: str

    class Thumbnail(attr.S):
        medium: str = attr.optional(str)
        small: str = attr.optional(str)
        tiny: str = attr.optional(str)

    manager = ClipManager()
    slug: str = attr.optional(str)
    broadcast_id: int = attr.optional(int)
    tracking_id: int = attr.optional(int)
    url: str = attr.optional(str)
    embed_url: str = attr.optional(str)
    embed_html: str = attr.optional(str)
    broadcaster: Broadcaster = attr.optional(Broadcaster)
    curator: Curator = attr.optional(Curator)
    vod: Vod = attr.optional(Vod)
    game: str = attr.optional(str)
    language: str = attr.optional(str)
    title: str = attr.optional(str)
    views: int = attr.optional(int)
    duration: float = attr.optional(float)
    created_at: str = attr.optional(str)
    thumbnails: Thumbnail = attr.optional(Thumbnail)

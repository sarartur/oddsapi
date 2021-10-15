from asyncio.events import get_event_loop
from aiohttp import ClientSession
from asyncio import new_event_loop
from functools import wraps
from typing import Optional, Dict

from .exceptions import OddsClientError
from ._types import Resource, OddsApiResponse

class Client:

    def __init__(self, aio=False) -> None:
        self.loop = get_event_loop()
        self.aio = aio

    @classmethod
    async def do_get_request(cls, self, resource):
        async with ClientSession(loop=self.loop) as session:
            async with session.get(
                url=self.host + resource.uri,
                params=resource.params,
                **resource.extra_kwargs
            ) as r:
                text = await r.text()
                if r.status != 200:
                    raise OddsClientError(status=r.status,
                        msg=text)
                self._set_requests_info(r.headers)
                return text, r.headers

    @classmethod
    async def handler(cls, self, func,  *args, **kwargs):
        resource = func(self, *args, **kwargs)
        text, headers = await Client.do_get_request(self, resource)
        return OddsApiResponse(text, headers)

    @classmethod
    def endpoint(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return cls.handler(self, func, *args, **kwargs) if self.aio else self.loop.run_until_complete(
                cls.handler(self, func, *args, **kwargs))
        return wrapper

class OddsApiClient(Client):

    host = "https://api.the-odds-api.com"

    def __init__(self, api_key) -> None:
        super().__init__()
        self.api_key = api_key
        self.requests_remaining = None
        self.requests_used = None

    def _set_requests_info(self, headers: Dict) -> None:
        self.requests_remaining = headers['X-Requests-Remaining']
        self.requests_used = headers['X-Requests-Used']

    @Client.endpoint
    def retrieve_sports(self):
        return Resource(uri = "/v3/sports/", params=dict(
            apiKey=self.api_key
        ))
    
    @Client.endpoint
    def retrieve_odds(self, sport_key:str, region:str, mkt:Optional[str] = 'h2h'):
        return Resource(uri = "/v3/odds/", params=dict(
            apiKey=self.api_key,
            sport=sport_key,
            region=region,
            mkt=mkt
        ))


# <============================================== IMPORTS =========================================================>
from aiohttp import ClientSession
from httpx import AsyncClient, Timeout
from Python_ARQ import ARQ

# <=============================================== SETUP ========================================================>
class State:
    _session = None
    _arq = None

    @classmethod
    async def get_session(cls):
        """ Lazily initializes and returns an aiohttp ClientSession. """
        if cls._session is None:
            cls._session = ClientSession()
        return cls._session

    @classmethod
    async def get_arq(cls):
        """ Lazily initializes and returns an ARQ client. """
        if cls._arq is None:
            session = await cls.get_session()
            cls._arq = ARQ("arq.hamker.dev", "RLWCED-WZASYO-AWOLTB-ITBWTP-ARQ", session)
        return cls._arq

# HTTPx Async Client
state = AsyncClient(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
    },
    timeout=Timeout(20),
)

# <===================================================== END ==================================================>

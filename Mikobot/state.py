import logging
from aiohttp import ClientSession
from httpx import AsyncClient, Timeout
from Python_ARQ import ARQ

# Setup logging
logging.basicConfig(level=logging.INFO)

# <=============================================== SETUP ========================================================>
class State:
    _session = None
    _arq = None

    @classmethod
    async def get_session(cls):
        """ Lazily initializes and returns an aiohttp ClientSession. """
        if cls._session is None:
            try:
                logging.info("Initializing a new aiohttp ClientSession.")
                cls._session = ClientSession()
            except Exception as e:
                logging.error(f"Failed to initialize ClientSession: {e}")
                raise
        return cls._session

    @classmethod
    async def get_arq(cls):
        """ Lazily initializes and returns an ARQ client. """
        if cls._arq is None:
            try:
                session = await cls.get_session()
                logging.info("Initializing ARQ client.")
                cls._arq = ARQ("arq.hamker.dev", "RLWCED-WZASYO-AWOLTB-ITBWTP-ARQ", session)
            except Exception as e:
                logging.error(f"Failed to initialize ARQ client: {e}")
                raise
        return cls._arq

# HTTPx Async Client with error handling
try:
    state = AsyncClient(
        http2=True,
        verify=True,  # Enable SSL verification for security
        headers={
            "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
        },
        timeout=Timeout(20),
    )
    logging.info("HTTPx Client initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize HTTPx Client: {e}")
    raise

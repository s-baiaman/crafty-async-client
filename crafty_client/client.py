import aiohttp

from .exceptions import (
        CraftyAuthError,
        CraftyPermissionError,
        CraftyNotFoundError,
        CraftyNetworkError
)

from .servers import ServersAPI


class CraftyClient:
    def __init__(self, base_url: str, api_token: str, timeout: float = 10.0, ssl: bool = True):
        self.base_url = base_url
        self._api_token = api_token
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._ssl = ssl

        self._session: aiohttp.ClientSession | None = None
        self.servers = ServersAPI(self)

    async def connect(self):
        self._session = aiohttp.ClientSession(timeout=self._timeout)

    async def close(self):
        if self._session:
            await self._session.close()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()


    async def _request(self, method: str, path: str, json=None, data=None, params=None):
        if not self._session:
            raise RuntimeError("Client not connected")

        url = f"{self.base_url}{path}"

        headers = {"Authorization": f"Bearer {self._api_token}"}

        try:
            async with self._session.request(method, url, headers=headers, json=json, data=data, params=params, ssl=False) as response:

                if response.status >= 400:
                    text = await response.text()
                    raise Exception(f"HTTP {response.status}: {text}")

                if response.status == 401:
                    raise CraftyAuthError("Invalid API token")

                if response.status == 403:
                    raise CraftyPermissionError("Forbidden")

                if response.status == 404:
                    raise CraftyNotFoundError("Not found")

                data = await response.json()

                return data.get("data")

        except aiohttp.ClientError as e:
            raise CraftyNetworkError(str(e))



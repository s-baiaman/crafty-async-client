from .models import Server


class ServersAPI:
    def __init__(self, client):
        self._client = client

    async def list_all(self) -> list[Server]:
        data = await self._client._request("GET", "/api/v2/servers")

        servers = []

        for item in data:
            servers.append(
                Server(
                    id=str(item["server_id"]),
                    name=item["server_name"],
                    running=item.get("running", False)
                )
            )

        return servers
    
    async def _action(self, server_id : str, action: str):
        await self._client._request("POST", f"/api/v2/servers/{server_id}/action/{action}")

    async def start(self, server_id: str):
        await self._action(server_id, "start_server")

    async def stop(self, server_id: str):
        await self._action(server_id, "stop_server")

    async def restart(self, server_id: str):
        await self._action(server_id, "restart_server")

    async def kill(self, server_id: str):
        await self._action(server_id, "kill_server")

    async def clone(self, server_id: str):
        await self._action(server_id, "clone_server")

    async def backup(self, server_id: str):
        await self._action(server_id, "backup_server")

    async def update_exe(self, server_id: str):
        await self._action(server_id, "update_executable")

    async def cmd(self, server_id: str, command: str):
        await self._client._request("POST", f"/api/v2/servers/{server_id}/stdin", data=command)

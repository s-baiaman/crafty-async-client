# Crafty Async Client

Async Python SDK for interacting with Crafty Controller API V2.

A lightweight and modern async wrapper for managing Minecraft servers via Crafty Controller.

---

[![Python](https://img.shields.io/badge/python-%3E%3D3.10-3776AB?logo=python&logoColor=white)](#)
[![GitHub Stars](https://img.shields.io/github/stars/s-baiaman/crafty-async-client?style=flat&color=FFD700&logo=starship&logoColor=white)](https://github.com/s-baiaman/crafty-async-client)
[![GitHub License](https://img.shields.io/github/license/henriquesebastiao/badges?style=flat&color=22c55e)](https://github.com/s-baiaman/crafty-async-client/blob/main/LICENSE)
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fs-baiaman%2Fcrafty-async-client&label=visitors&countColor=%230c7ebe&style=flat&labelStyle=none)

---

## 🚀 What is this?

This library provides a simple async interface to control Crafty Controller servers:

- Start / stop / restart servers
- Send console commands
- Fetch server information
- Built on top of aiohttp

---

## ⚡ Features

- Fully async (built on `asyncio`)
- Simple and minimal API
- Token-based authentication
- Lightweight (no heavy dependencies)
- Designed for automation and bots

---

## 📦 Installation
```bash
pip install crafty-async-client
```

## ⚡Quick Start
```python3
import asyncio
from crafty_client import CraftyClient

async def main():
    async with CraftyClient(
        "https://your-host:8443",
        "your_api_token",
        ssl=False
    ) as client:

        servers = await client.servers.list_all()

        for server in servers:
            print(server)

        if servers:
            server = servers[0]

            await client.servers.start(server.id)
            await client.servers.cmd(server.id, "say Hello World!")

asyncio.run(main())
```

## 📌 Example use case
```python3
# restart all servers
for server in servers:
    await client.servers.restart(server.id)
```

## 📄 License
MIT License — Copyright (c) 2026 Baiaman Sun. See [LICENSE](https://github.com/s-baiaman/crafty-async-client/blob/main/LICENSE) for the full text.

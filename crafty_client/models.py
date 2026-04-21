from dataclasses import dataclass


@dataclass
class Server:
    id: str
    name: str
    running: bool


from starlette.websockets import WebSocket
from typing import Dict, Any

class ConnectionManager:
    def __init__(self):
        self.rooms: Dict[str, Dict[str, WebSocket]] = {}

    async def connect(self, room: str, username: str, websocket: WebSocket):
        await websocket.accept()
        self.rooms.setdefault(room, {})
        self.rooms[room][username] = websocket
        await self.broadcast_users(room)

    def disconnect(self, room: str, username: str):
        if room in self.rooms:
            self.rooms[room].pop(username, None)

    async def broadcast_users(self, room: str) -> None:
        users = list(self.rooms[room].keys())
        for ws in self.rooms[room].values():
            await ws.send_json({"type": "users", "users": users})

    async def broadcast_message(self, room: str, message: Dict[str, Any]):
        for ws in self.rooms[room].values():
            await ws.send_json({"type": "message", **message})

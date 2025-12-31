from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from database import engine, SessionLocal
from models import Base, User, Room, Message
from websocket_manager import ConnectionManager
from datetime import datetime, timezone

app = FastAPI()
manager = ConnectionManager()

Base.metadata.create_all(bind=engine)

@app.websocket("/ws/{room}/{username}")
async def websocket_endpoint(websocket: WebSocket, room: str, username: str):
    db = SessionLocal()

    # Get or create user
    user = db.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Get or create room
    chat_room = db.query(Room).filter_by(name=room).first()
    if not chat_room:
        chat_room = Room(name=room)
        db.add(chat_room)
        db.commit()
        db.refresh(chat_room)

    await manager.connect(room, username, websocket)

    try:
        while True:
            text = await websocket.receive_text()
            if not text.strip():
                continue

            msg = Message(
                content=text,
                user_id=user.id,
                room_id=chat_room.id
            )
            db.add(msg)
            db.commit()

            await manager.broadcast_message(room, {
                "username": username,
                "content": text,
                "timestamp": datetime.now(timezone.utc).strftime("%H:%M")
            })

    except WebSocketDisconnect:
        manager.disconnect(room, username)
        await manager.broadcast_users(room)
        db.close()

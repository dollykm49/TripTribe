# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routes import auth_router
from app.users.routes import user_router
from app.trips.routes import trip_router
from app.wallet.routes import wallet_router
from app.bulletin.routes import bulletin_router
from app.chat.routes import chat_router
from app.matching.routes import match_router
from app.db.session import init_db
from app.group_wallet.routes import group_wallet_router
app = FastAPI(title="TripTribe API")

# 🛡️ CORS
origins = ["http://localhost:3000", "http://localhost:8081"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚀 Startup DB
@app.on_event("startup")
def on_startup():
    init_db()

# 🧩 Routers
app.include_router(auth_router, prefix="/api/auth")
app.include_router(user_router, prefix="/api/users")
app.include_router(trip_router, prefix="/api/trips")
app.include_router(wallet_router, prefix="/api/wallet")
app.include_router(bulletin_router, prefix="/api/bulletin")
app.include_router(chat_router, prefix="/api/chat")
app.include_router(match_router, prefix="/api/matching")
app.include_router(group_wallet_router, prefix="/api/group-wallet")

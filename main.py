from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ms_core import setup_app

from app.settings import db_url

application = FastAPI(
    title="ploshtadka-payments-ms",
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tortoise_conf = setup_app(
    application, db_url, Path("app") / "routers", ["app.models"]
)

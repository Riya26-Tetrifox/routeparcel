from fastapi import FastAPI
from backend import models
from backend.database import engine
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from backend.routers import getusers,users
app=FastAPI()
origins=[
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
FastAPIInstrumentor.instrument_app(app)
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
app.include_router(getusers.router)
app.include_router(users.router)
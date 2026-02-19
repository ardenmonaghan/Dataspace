from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db_helpers import db_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(db_routes.router)



# uvicorn main:app --reload
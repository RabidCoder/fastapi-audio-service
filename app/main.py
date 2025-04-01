from fastapi import FastAPI

from app.api import audio, auth, users
from app.db.session import get_db

app = FastAPI(title='FastAPI Audio Service', version='1.0')

@app.get('/')
async def root():
    return {'message':'Welcome to FastAPI Audio Service!'}

app.include_router(audio.router, prefix='/audio', tags=['audio'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(users.router, prefix='/users', tags=['users'])

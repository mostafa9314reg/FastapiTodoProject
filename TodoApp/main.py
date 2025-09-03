from fastapi import FastAPI,Depends
from typing import Annotated
from sqlalchemy.orm import session
import models
from fastapi.responses import HTMLResponse, RedirectResponse
from models import Todos
from database import engine,SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    


db_dependency = Annotated[session,Depends(get_db)]


@app.get("/")
async def read_all_books(db:db_dependency):
   return db.query(Todos).all()


# @app.get("/", include_in_schema=False)
# def home():
#     # Option A: show something
#     return HTMLResponse("<h2>FastAPI is running ✅</h2><p>See <a href='/docs'>/docs</a></p>")



# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"status": "ok"}
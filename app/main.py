from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import engine, SessionLocal

# Создаем таблицы в базе данных при запуске
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Catalog API")

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в каталог фильмов!"}

# 1. Добавить фильм (Create)
@app.post("/movies/", response_model=schemas.MovieResponse)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# 2. Получить список всех фильмов (Read)
@app.get("/movies/", response_model=List[schemas.MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()
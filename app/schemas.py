from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Название фильма")
    genre: str = Field(..., description="Жанр")
    release_year: int = Field(..., ge=1888, description="Год выпуска")
    rating: float = Field(..., ge=0, le=10, description="Рейтинг от 0 до 10")
    director: str = Field(..., description="Режиссер")

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True
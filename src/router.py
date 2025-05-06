from fastapi import APIRouter, HTTPException
from src.logic import get_users, get_user_by_id, get_badges, get_achievements, get_missions, get_events
from src.models.gamification import User, Badge, Achievement, Mission, Event
from typing import List

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users():
    return get_users()

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: str):
    user = get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.get("/badges", response_model=List[Badge])
def read_badges():
    return get_badges()

@router.get("/achievements", response_model=List[Achievement])
def read_achievements():
    return get_achievements()

@router.get("/missions", response_model=List[Mission])
def read_missions():
    return get_missions()

@router.get("/events", response_model=List[Event])
def read_events():
    return get_events()

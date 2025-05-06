from src.models.gamification import User, Badge, Achievement, Mission, Event
from typing import List, Optional
from datetime import datetime

users = [
    User(id="1", name="Alice"),
    User(id="2", name="Bob"),
]

badges = [
    Badge(id="1", name="Iniciante", description="Primeiro passo na jornada."),
    Badge(id="2", name="Veterano", description="Experiente na plataforma."),
]

achievements = [
    Achievement(id="1", name="Conquista 1", description="Descrição da conquista 1", condition="condição 1", points_reward=10),
    Achievement(id="2", name="Conquista 2", description="Descrição da conquista 2", condition="condição 2", points_reward=20),
]

missions = [
    Mission(id="1", title="Missão 1", description="Descrição da missão 1", xp_reward=50),
    Mission(id="2", title="Missão 2", description="Descrição da missão 2", xp_reward=100),
]

events = [
    Event(id="1", user_id="1", type="login", metadata={"info": "Primeiro login"}),
    Event(id="2", user_id="2", type="compra", metadata={"item": "Produto X"}),
]

def get_users() -> List[User]:
    return users

def get_user_by_id(user_id: str) -> Optional[User]:
    return next((user for user in users if user.id == user_id), None)

def get_badges() -> List[Badge]:
    return badges

def get_achievements() -> List[Achievement]:
    return achievements

def get_missions() -> List[Mission]:
    return missions

def get_events() -> List[Event]:
    return events

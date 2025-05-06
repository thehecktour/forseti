from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class User:
    id: str
    name: str
    points: int = 0
    level: int = 1
    badges: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Badge:
    id: str
    name: str
    description: str
    icon_url: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Achievement:
    id: str
    name: str
    description: str
    condition: str
    points_reward: int
    badge_id: Optional[str] = None


@dataclass
class Mission:
    id: str
    title: str
    description: str
    xp_reward: int
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Event:
    id: str
    user_id: str
    type: str
    metadata: dict
    timestamp: datetime = field(default_factory=datetime.utcnow)

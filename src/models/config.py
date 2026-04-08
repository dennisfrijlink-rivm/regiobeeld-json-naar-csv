from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    config_id: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    duiding: Optional[str] = None
    credits_id: Optional[str] = None
    update_datum: Optional[str] = None
    group: Optional[str] = None
    order: Optional[str] = None

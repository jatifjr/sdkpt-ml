from typing import Any, Optional, List

from pydantic import BaseModel


class SemarBetulAuthBase(BaseModel):
    username: str
    password: str


class SemarBetulAuthCreate(BaseModel):
    id: str
    access_token: str


class SemarBetulAuth(BaseModel):
    access_token: str

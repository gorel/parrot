#!/usr/bin/env python3

from typing import List, Optional

from pydantic import BaseModel

from parrot.entity.schema.player import Player
from parrot.entity.schema.voting_mode import VotingMode


class GameLobby(BaseModel):
    instance_id: str
    team1_name: str
    team2_name: str
    voting_mode: VotingMode
    guess_timeout: Optional[int]
    team1_players: List[Player]
    team2_players: List[Player]
    started: bool

    class Config:
        orm_mode = True

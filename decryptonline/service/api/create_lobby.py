#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional

from decryptonline.entity.game_lobby import GameLobby
from decryptonline.entity.model.voting_mode import VotingMode


@dataclass
class CreateLobbyRequest:
    team1_name: str
    team2_name: str
    voting_mode: VotingMode
    guess_timeout: Optional[int]


@dataclass
class CreateLobbyResponse:
    lobby: GameLobby

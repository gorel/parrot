#!/usr/bin/env python3

from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Card:
    text: str

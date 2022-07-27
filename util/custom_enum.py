from enum import Enum


class CurrentState(Enum):
    IDLE = 1
    ATTACK = 2
    ATTACK_STANDBY = 3
    DEAD = 4
    DYING = 5
    JUMP = 6
    LIMIT_BREAK = 7
    MAGIC_ATTACK = 8
    MAGIC_STANDBY = 9
    MOVE = 10
    WIN = 11
    WIN_END = 12


class PlayerSide(Enum):
    RIGHT = 1
    LEFT = 2

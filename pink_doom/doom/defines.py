"""
`doomdef.h`.

Internally used data structures for virtually everything,
key definitions, lots of other stuff.
"""
from enum import Enum, auto

# Global parameters/defines.

VERSION = 110
"""DOOM version."""


class GameMode(Enum):
    """
    Game mode handling.

    Identify IWAD version to handle IWAD dependent animations, etc.
    """

    SHAREWARE = auto()
    """DOOM 1 shareware, E1, M9"""
    REGISTERED = auto()
    """DOOM 1 registered, E3, M27"""
    COMMERCIAL = auto()
    """DOOM 2 retail, E1 M34"""
    # DOOM 2 german edition not handled
    RETAIL = auto()
    """
    DOOM 1 retail, E4, M36.

    Also known as "The Ultimate DOOM".
    """
    INDETERMINED = auto()
    """Well, no IWAD found."""


class GameMission(Enum):
    """Mission packs - might be useful for TC stuff."""

    DOOM = auto()
    """DOOM 1"""
    DOOM2 = auto()
    """DOOM 2"""
    PACK_TNT = auto()
    """TNT mission pack"""
    PACK_PLUT = auto()
    """Plutonia pack"""
    NONE = auto()


class Language(Enum):
    """Identify language to use, software localization."""

    ENGLISH = auto()
    FRENCH = auto()
    GERMAN = auto()
    UNKNOWN = auto()


RANGECHECK = True
"""If ``RANGECHECK == False``, most parameter debugging code will not run."""

BASE_WIDTH = 320
"""
For resize of screen, at start of game.

It will not work dynamically, see visplanes.
"""

SCREEN_MUL = 1
"""
It is educational but futile to change this scaling e.g. to 2.

Drawing of status bar, menus etc. is tied to the scale implied
by the graphics.
"""

INV_ASPECT_RATIO = 0.625
"""0.75, ideally."""

SCREEN_WIDTH = 320
"""``SCREEN_MUL * BASE_WIDTH == 320``"""
SCREEN_HEIGHT = 200
"""``SCREEN_MUL * BASE_WIDTH * INV_ASPECT_RATIO == 200``"""

MAX_PLAYERS = 1
"""The maximum number of players, this sourceport is singleplayer only."""

TIC_RATE = 35
"""State updates, number of tics / second."""


class GameState(Enum):
    """
    The current state of the game.

    Whether we are playing, gazing at the intermission screen,
    the game final animation, or a demo.
    """

    LEVEL = auto()
    INTERMISSION = auto()
    FINALE = auto()
    DEMO_SCREEN = auto()
    WIPE = auto()


class MapThingFlag(Enum):
    """Difficulty/skill settings/filters."""

    # Skill flags.
    EASY = 0x1
    NORMAL = 0x2
    HARD = 0x4

    AMBUSH = 0x8
    """Deaf monsters/do not react to sound."""


class Skill(Enum):
    """The selected skill."""

    BABY = auto()
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    NIGHTMARE = auto()


class Card(Enum):
    """Key cards."""

    BLUE_CARD = auto()
    YELLOW_CARD = auto()
    RED_CARD = auto()
    BLUE_SKULL = auto()
    YELLOW_SKULL = auto()
    RED_SKULL = auto()

    NUM_CARDS = auto()


class WeaponType(Enum):
    """
    The defined weapons.

    Includes a marker indicating the user has not changed weapon.
    """

    FIST = auto()
    PISTOL = auto()
    SHOTGUN = auto()
    CHAINGUN = auto()
    MISSILE = auto()
    PLASMA = auto()
    BFG = auto()
    CHAINSAW = auto()
    SUPER_SHOTGUN = auto()

    NUM_WEAPONS = auto()

    NO_CHANGE = auto()
    """No pending weapon change."""


class AmmoType(Enum):
    """Ammunition types defined."""

    CLIP = auto()
    """Pistol/chaingun ammo."""
    SHELL = auto()
    """Shotgun/double-barreled shotgun."""
    CELL = auto()
    """Plasma rifle, BFG."""
    MISL = auto()
    """Missile launcher."""

    NUM_AMMO = auto()

    NO_AMMO = auto()
    """Unlimited for chainsaw/fist."""


class PowerType(Enum):
    """Power-up artifacts."""

    INVULNERABILITY = auto()
    STRENGTH = auto()
    INVISIBILITY = auto()
    IRON_FEET = auto()
    ALL_MAP = auto()
    INFRARED = auto()

    NUM_POWERS = auto()


class PowerDuration(Enum):
    """
    Power-up durations.

    Counts the ticks till expiration.
    """

    INVULN_TICS = 30 * TIC_RATE
    INVIS_TICS = 60 * TIC_RATE
    INFRA_TICS = 120 * TIC_RATE
    IRON_TICS = 60 * TIC_RATE

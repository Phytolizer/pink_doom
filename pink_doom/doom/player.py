"""The Doom player structure."""


class Player:
    """Represents the player's perspective as an object in the map."""

    def __init__(self):
        """
        Create a new player object.

        This is only likely to happen during global initialization.
        """
        pass


class WbPlayerStruct:
    """Represents a player's intermission stats."""

    in_game: bool
    kills: int
    items: int
    secrets: int
    time: int
    score: int


class PlayerStatistics:
    """Holds the player's score."""

    epsd: int
    did_secret: bool
    """If true, show the secret level instead of the regular next level."""
    last_level: int
    next_level: int

    max_kills: int
    max_items: int
    max_secret: int

    par_time: int

    plyr: WbPlayerStruct

    def __init__(self):
        """
        Create a new statistics object.

        It will be initialized to all zero values until a level actually starts.
        """
        self.epsd = 0
        self.did_secret = False

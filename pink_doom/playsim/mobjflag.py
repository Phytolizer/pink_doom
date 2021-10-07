"""Contains just MapObjectFlag, to avoid circular dependencies."""
from enum import Flag


class MapObjectFlag(Flag):
    """Misc. mobj flags."""

    NONE = 0x0
    """None of the below."""
    SPECIAL = 0x1
    """Call P_SpecialThing when touched."""
    SOLID = 0x2
    """Blocks."""
    SHOOTABLE = 0x4
    """Can be hit."""
    NOSECTOR = 0x8
    """Don't use the sector links (invisible but touchable)."""
    NOBLOCKMAP = 0x10
    """Don't use the blocklinks (inert but displayable)."""
    AMBUSH = 0x20
    """Not to be activated by sound, deaf monster."""
    JUSTHIT = 0x40
    """Will try to attach right back."""
    JUSTATTACKED = 0x80
    """Will take at least one step before attacking."""
    SPAWNCEILING = 0x100
    """
    On level spawning (initial position),
    hang from ceiling instead of standing on floor.
    """
    NOGRAVITY = 0x200
    """
    Don't apply gravity (every tic),
    that is, object will float, keeping current height
    or changing it actively.
    """
    DROPOFF = 0x400
    """This allows jumps from high places."""
    PICKUP = 0x800
    """For players, will pick up items."""
    NOCLIP = 0x1000
    """Player cheat."""
    SLIDE = 0x2000
    """Player: keep info about sliding along walls."""
    FLOAT = 0x4000
    """
    Allows moves to any height, no gravity.

    For active floaters, e.g. cacodemons, pain elementals.
    """
    TELEPORT = 0x8000
    """Don't cross lines or look at heights on teleport."""
    MISSILE = 0x10000
    """
    Don't hit same species, explode on block.

    Player missiles as well as fireballs of various kinds.
    """
    DROPPED = 0x20000
    """
    Dropped by a demon, not level spawned.

    E.g. ammo clips dropped by dying former humans.
    """
    SHADOW = 0x40000
    """
    Use fuzzy draw.

    E.g. shadow demons (spectres), temporary player invisibility powerup.
    """
    NOBLOOD = 0x80000
    """
    Flag: don't bleed when shot (use puff).

    Barrels and shootable furniture shall not bleed.
    """
    CORPSE = 0x100000
    """
    Don't stop moving halfway off a step.

    Have dead bodies slide down all the way.
    """
    INFLOAT = 0x200000
    """Floating to a height for a move, don't auto-float to target's height."""
    COUNTKILL = 0x400000
    """
    On kill, count this enemy object towards intermission kill total.

    Happy gathering.
    """
    COUNTITEM = 0x800000
    """On picking up, count this item object towards intermission item total."""
    SKULLFLY = 0x1000000
    """
    Special handling: skull in flight.

    Neither a cacodemon nor a missile.
    """

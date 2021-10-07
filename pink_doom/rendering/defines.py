"""Rendering module, shared data struct definitions."""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Optional

from pink_doom.doom.data import NodeFlag
from pink_doom.misc.fixed import Fixed
from pink_doom.playsim.mobj import MapObject


class Silhouette(Enum):
    """
    Silhouette.

    Needed for clipping segs (mainly) and sprites representing things.
    """

    NONE = 0b00
    BOTTOM = 0b01
    TOP = 0b10
    BOTH = 0b11


MAX_DRAW_SEGS = 256


# INTERNAL MAP TYPES
# used by play and refresh


@dataclass
class Vertex:
    """
    Your plain vanilla vertex.

    Note: transformed values not buffered locally,
    like some DOOM-alikes ("wt", "WebView") did.
    """

    x: Fixed
    y: Fixed


@dataclass
class DegeneratedMapObject:
    """
    Each sector has a ``degenmobj_t`` in its center for sound origin purposes.

    I suppose this does not handle sound from moving objects (doppler),
    because position is prolly just buffered, not updated.
    """

    x: int
    y: int
    z: int


@dataclass
class Sector:
    """
    The SECTORS record, at runtime.

    Stores things/mobjs.
    """

    floor_height: Fixed
    ceiling_height: Fixed
    floor_pic: int
    ceiling_pic: int
    light_level: int
    special: int
    tag: int

    sound_traversed: int
    """0 = untraversed, 1,2 = sndlines -1"""

    sound_target: Optional[MapObject]
    """thing that made a sound (or null)"""

    blockbox: tuple[int, int, int, int]
    """mapblock bounding box for height changes"""

    soundorg: DegeneratedMapObject
    """origin for any sounds played by the sector"""

    validcount: int
    """if == validcount, already checked"""

    thinglist: list[MapObject]
    """list of mobjs in sector"""

    specialdata: Any
    """Thinker for reversible actions"""

    lines: list["Line"]


@dataclass
class Side:
    """The SideDef."""

    textureoffset: Fixed
    """add this to the calculated texture column"""

    rowoffset: Fixed
    """add this to the calculated texture top"""

    # Texture indices.
    # We do not maintain names here.
    toptexture: int
    bottomtexture: int
    midtexture: int

    sector: Sector
    """Sector the SideDef is facing."""


class SlopeType(Enum):
    """Move clipping aid for LineDefs."""

    HORIZONTAL = auto()
    VERTICAL = auto()
    POSITIVE = auto()
    NEGATIVE = auto()


@dataclass
class Line:
    """A LineDef."""

    # Vertices, from v1 to v2.
    v1: Vertex
    v2: Vertex

    # Precalculated v2 - v1 for side checking.
    dx: Fixed
    dy: Fixed

    # Animation related.
    flags: int
    special: int
    tag: int

    sidenum: tuple[int, int]
    """
    Visual appearance: SideDefs.

    sidenum[1] will be -1 if one-sided.
    """

    bbox: tuple[Fixed, Fixed, Fixed, Fixed]
    """Another bounding box, for the extent of the LineDef."""

    slopetype: SlopeType
    """To aid move clipping."""

    # Front and back sector.
    # Note: redundant? Can be retrieved from SideDefs.
    frontsector: Sector
    backsector: Sector

    validcount: int
    """If == validcount, already checked."""

    specialdata: Any
    """Thinker for reversible actions."""


@dataclass
class SubSector:
    """
    A SubSector.

    References a Sector.
    Basically, this is a list of LineSegs,
    indicating the visible walls that define
    (all or some) sides of a convex BSP leaf.
    """

    sector: Sector
    numlines: int
    firstline: int


@dataclass
class Seg:
    """The LineSeg."""

    v1: Vertex
    v2: Vertex

    offset: Fixed

    angle: int

    sidedef: Side
    linedef: Line

    # Sector references.
    # Could be retrieved from linedef, too.
    frontsector: Sector
    backsector: Optional[Sector]
    """None if one-sided."""


@dataclass
class Node:
    """BSP node."""

    x: Fixed
    y: Fixed
    dx: Fixed
    dy: Fixed

    bbox: tuple[
        tuple[Fixed, Fixed],
        tuple[Fixed, Fixed],
        tuple[Fixed, Fixed],
        tuple[Fixed, Fixed],
    ]
    """Bounding box for each child."""

    children: tuple[NodeFlag, NodeFlag]
    """If SUBSECTOR, it's a subsector."""

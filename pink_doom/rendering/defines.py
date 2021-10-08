"""Rendering module, shared data struct definitions."""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Optional

from pink_doom.doom.data import NodeFlag
from pink_doom.doom.defines import SCREEN_WIDTH
from pink_doom.misc.fixed import Fixed
from pink_doom.playsim.mobj import MapObject
from pink_doom.playsim.mobjflag import MapObjectFlag


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


@dataclass
class Post:
    """A run of non-masked source pixels."""

    topdelta: int
    """-1 is the last post in a column."""
    length: int
    """``length`` data bytes follows."""


Column = list[Post]


# OTHER TYPES


LightTable = int


@dataclass
class DrawSeg:
    """Docs just say "?"."""

    curline: Seg
    x1: int
    x2: int

    scale1: Fixed
    scale2: Fixed

    silhouette: Silhouette

    bsilheight: Fixed
    """Do not clip sprites above this."""

    tsilheight: Fixed
    """Do not clip sprites below this."""

    # Lists for sprite clipping.
    sprtopclip: list[int]
    sprbottomclip: list[int]
    maskedtexturecol: list[int]


@dataclass
class Patch:
    """
    A patch holds one or more columns.

    Patches are used for sprites and all masked pictures,
    and we compose textures from the TEXTURE1/2 lists
    of patches.
    """

    width: int
    height: int
    leftoffset: int
    """pixels to the left of origin"""
    topoffset: int
    """pixels below the origin"""

    columnofs: list[int]
    """length == ``width``"""


@dataclass
class VisSprite:
    """
    A vissprite_t is a thing that will be drawn during a refresh.

    I.e. a sprite object that is partly visible.
    """

    x1: int
    x2: int

    # for line side calculation
    gx: Fixed
    gy: Fixed

    # global bottom/top for silhouette clipping
    gz: Fixed
    gzt: Fixed

    startfrac: Fixed
    """horizontal position of x1"""

    scale: Fixed

    xiscale: Fixed
    """negative if flipped"""

    texturemid: Fixed
    patch: int

    colormap: LightTable
    """for color translation and shadow draw, maxbright frames as well"""

    mobjflags: MapObjectFlag


@dataclass
class SpriteFrame:
    """
    Sprites are patches with a special naming convention.

    This naming convention is so that they can be recognized by
    :func:`pink_doom.rendering.init.init_sprites`.

    The base name is ``NNNNFx`` or ``NNNNFxFx``, with x indicating
    the rotation, x = 0, 1-7.

    The sprite and frame specified by a Thing is range-checked at runtime.

    A sprite is a Patch that is assumed to represent a 3D object
    and may have multiple rotations pre-drawn.

    Horizontal flipping is used to save space, thus ``NNNNF2F5`` defines a
    mirrored patch.

    Some sprites will only have one picture used for all views: ``NNNNF0``
    """

    rotate: bool
    """If false, use 0 for any position."""

    lump: tuple[8 * (int,)]
    """Lump to use for view angles 0-7."""

    flip: tuple[8 * (bool,)]
    """Flip bit to use for view angles 0-7."""


@dataclass
class SpriteDef:
    """A sprite definition: a number of animation frames."""

    frames: list[SpriteFrame]


@dataclass
class Visplane:
    """
    A visplane.

    Now what is a visplane, anyway?
    """

    height: Fixed
    picnum: int
    lightlevel: int
    minx: int
    maxx: int

    # Here lies the rub for all dynamic resize / change of resolution.
    top: tuple[SCREEN_WIDTH * (int,)]
    bottom: tuple[SCREEN_WIDTH * (int,)]

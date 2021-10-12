"""
Rendering main loop and setup functions, utility functions.

BSP, geometry, trigonometry.

See :mod:`pink_doom.misc.tables`, too.
"""

from typing import Callable, Optional

from pink_doom.doom.defines import SCREEN_WIDTH
from pink_doom.misc.bbox import BoxCoord
from pink_doom.misc.fixed import FRAC_BITS, Fixed, fixed_div, fixed_mul
from pink_doom.misc.tables import (
    ANG90,
    ANG180,
    ANG270,
    ANGLE_TO_FINE_SHIFT,
    DBITS,
    FINE_ANGLES,
    fine_sine,
    slope_div,
    tan_to_angle,
)
from pink_doom.pink_doom.doom.player import Player
from pink_doom.rendering.defines import LightTable, Node, Seg

_FIELDOFVIEW = 2048
"""Fineangles in the :var:`SCREEN_WIDTH` wide window."""

_view_angle_offset = 0
validcount = 1
"""increment every time a check is made"""

fixed_colormap: Optional[LightTable] = None

centerx = 0
centery = 0

centerxfrac: Fixed = 0
centeryfrac: Fixed = 0
projection: Fixed = 0

framecount = 0

sscount = 0
linecount = 0
loopcount = 0

viewx: Fixed = 0
viewy: Fixed = 0
viewz: Fixed = 0

viewangle = 0

viewcos: Fixed = 0
viewsin: Fixed = 0

viewplayer: Optional[Player] = None

detailshift = 0
"""0 = high, 1 = low"""

clipangle = 0

viewangletox: list[int] = [0 for _ in range(FINE_ANGLES // 2)]
"""
Maps the visible view angles to screen X coordinates.

Flattens the arc to a flat projection plane.
There will be many angles mapped to the same X.
"""

xtoviewangle: list[int] = [0 for _ in range(SCREEN_WIDTH + 1)]
"""
Maps a screen pixel to the lowest viewangle that maps back to x.

Ranges from ``clipangle`` to ``-clipangle``.
"""

fine_cosine = fine_sine[FINE_ANGLES // 4 :]

LIGHTLEVELS = 16
"""Now why not 32 here?"""
LIGHTSEGSHIFT = 4

MAXLIGHTSCALE = 48
LIGHTSCALESHIFT = 12
MAXLIGHTZ = 128
LIGHTZSHIFT = 20

scalelight: list[list[Optional[LightTable]]] = [
    [None for _ in range(LIGHTLEVELS)] for _ in range(MAXLIGHTSCALE)
]
scalelightfixed: list[Optional[LightTable]] = [None for _ in range(MAXLIGHTSCALE)]
zlight: list[list[Optional[LightTable]]] = [
    [None for _ in range(LIGHTLEVELS)] for _ in range(MAXLIGHTZ)
]

extralight = 0

colfunc: Optional[Callable] = None
basecolfunc: Optional[Callable] = None
fuzzcolfunc: Optional[Callable] = None
transcolfunc: Optional[Callable] = None
spanfunc: Optional[Callable] = None


def add_point_to_box(x: int, y: int, box: list[Fixed]) -> None:
    """Expand a given bbox so it encloses a given point."""
    if x < box[BoxCoord.LEFT]:
        box[BoxCoord.LEFT] = x
    if x > box[BoxCoord.RIGHT]:
        box[BoxCoord.RIGHT] = x
    if y < box[BoxCoord.BOTTOM]:
        box[BoxCoord.BOTTOM] = y
    if y > box[BoxCoord.TOP]:
        box[BoxCoord.TOP] = y


def point_on_side(x: Fixed, y: Fixed, node: Node) -> bool:
    """
    Traverse BSP (sub)tree, check point against partition plane.

    Returns side 0 (front) or 1 (back).

    (Python note: this function returns a bool, mapping 0 to false
    and 1 to true.)
    """
    if node.dx == 0:
        if x <= node.x:
            return node.dy > 0
        return node.dy < 0
    if node.dy == 0:
        if y <= node.y:
            return node.dx < 0
        return node.dx > 0

    dx = x - node.x
    dy = y - node.y

    # Try to quickly decide by looking at sign bits.
    if (node.dy ^ node.dx ^ dx ^ dy) < 0:
        return (node.dy ^ dx) < 0

    # TODO(Phytolizer) why do we shift here?
    left = fixed_mul(node.dy >> FRAC_BITS, dx)
    right = fixed_mul(dy, node.dx >> FRAC_BITS)

    return right >= left


def point_on_seg_side(x: Fixed, y: Fixed, line: Seg) -> bool:
    """See :func:`point_on_side`."""
    lx = line.v1.x
    ly = line.v1.y

    ldx = line.v2.x - lx
    ldy = line.v2.y - ly

    if ldx == 0:
        if x <= lx:
            return ldy > 0
        return ldy < 0

    if ldy == 0:
        if y <= ly:
            return ldx < 0
        return ldx > 0

    dx = x - lx
    dy = y - ly

    # Try to quickly decide by looking at sign bits.
    if (ldy ^ ldx ^ dx ^ dy) < 0:
        return (ldy ^ dx) < 0

    left = fixed_mul(ldy >> FRAC_BITS, dx)
    right = fixed_mul(dy, ldx >> FRAC_BITS)

    return right >= left


def point_to_angle(x: Fixed, y: Fixed) -> int:
    """
    Get a global angle from cartesian coordinates.

    The coordinates are flipped until they are in the first octant of
    the coordinate system, then the y (<= x) is scaled and divided by x
    to get a tangent (slope) value which is looked up in the
    :var:`pink_doom.misc.tables.tan_to_angle` table.
    """
    x -= viewx
    y -= viewy

    if x == 0 and y == 0:
        return 0

    if x >= 0:
        if y >= 0:
            if x > y:
                # octant 0
                return tan_to_angle[slope_div(y, x)]
            # octant 1
            return ANG90 - 1 - tan_to_angle[slope_div(x, y)]
        # y < 0
        y = -y
        if x > y:
            # octant 8
            return -tan_to_angle[slope_div(y, x)]
        # octant 7
        return ANG270 + tan_to_angle[slope_div(x, y)]
    # x < 0
    x = -x
    if y >= 0:
        if x > y:
            # octant 3
            return ANG180 - 1 - tan_to_angle[slope_div(y, x)]
        # octant 2
        return ANG90 + tan_to_angle[slope_div(x, y)]
    # y < 0
    y = -y
    if x > y:
        # octant 4
        return ANG180 + tan_to_angle[slope_div(y, x)]
    # octant 5
    return ANG270 - 1 - tan_to_angle[slope_div(x, y)]


def point_to_angle_2(x1: Fixed, y1: Fixed, x2: Fixed, y2: Fixed) -> int:
    """See :func:`point_to_angle`."""
    global viewx, viewy
    viewx = x1
    viewy = y1
    return point_to_angle(x2, y2)


def point_to_dist(x: Fixed, y: Fixed) -> Fixed:
    """Get the distance from (``viewx``, ``viewy``)."""
    dx = abs(x - viewx)
    dy = abs(y - viewy)

    if dy > dx:
        dx, dy = dy, dx

    angle = (tan_to_angle[fixed_div(dy, dx) >> DBITS] + ANG90) >> ANGLE_TO_FINE_SHIFT

    return fixed_div(dx, fine_sine[angle])


# TODO
# def scale_from_global_angle(visangle: int) -> Fixed:
#     """
#     Return the texture mapping scale for the current line at the given angle.

#     ``rw_distance`` must be calculated first.
#     """
#     anglea = ANG90 + (visangle - viewangle)
#     angleb = ANG90 + (visangle - rw_normalangle)

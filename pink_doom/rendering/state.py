"""Rendering internal state variables (global)."""

from typing import Optional

from pink_doom.doom.player import Player
from pink_doom.misc.fixed import Fixed
from pink_doom.misc.tables import FINE_ANGLES
from pink_doom.rendering.defines import (
    SCREEN_WIDTH,
    LightTable,
    Line,
    Node,
    Sector,
    Seg,
    Side,
    SpriteDef,
    SubSector,
    Vertex,
    Visplane,
)

textureheight: list[Fixed] = []
"""Needed for texture pegging."""

spritewidth: list[Fixed] = []
"""Needed for pre-rendering (fracs)."""

spriteoffset: list[Fixed] = []
spritetopoffset: list[Fixed] = []

colormaps: list[LightTable] = []

viewwidth: int = 0
scaledviewwidth: int = 0
viewheight: int = 0

firstflat: int = 0

# for global animation
flattranslation: list[int] = []
texturetranslation: list[int] = []

# sprite...
firstspritelump: int = 0
lastspritelump: int = 0
numspritelumps: int = 0

# lookup tables for map data
numsprites: int = 0
sprites: list[SpriteDef] = []

numvertexes: int = 0
vertexes: list[Vertex] = []

numsegs: int = 0
segs: list[Seg] = []

numsectors: int = 0
sectors: list[Sector] = []

numsubsectors: int = 0
subsectors: list[SubSector] = []

numnodes: int = 0
nodes: list[Node] = []

numlines: int = 0
lines: list[Line] = []

numsides: int = 0
sides: list[Side] = []

# POV data
viewx: Fixed = 0
viewy: Fixed = 0
viewz: Fixed = 0

viewangle: int = 0
viewplayer: Optional[Player] = None

clipangle: int = 0

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

rw_distance: Fixed = 0
rw_normalangle: int = 0

rw_angle1: int = 0

sscount: int = 0

floorplane: Optional[Visplane] = None
ceilingplane: Optional[Visplane] = None

"""System-specific interface stuff."""
import sys
from typing import Optional

from pink_doom.doom.defines import RANGECHECK, SCREEN_HEIGHT, SCREEN_WIDTH
from pink_doom.misc.fixed import Fixed
from pink_doom.rendering.defines import LightTable

MAXWIDTH = 1120
MAXHEIGHT = 832

ylookup: list[list[int]] = [[] for _ in range(MAXHEIGHT)]
columnofs: list[int] = [0 for _ in range(MAXWIDTH)]

dc_colormap: Optional[LightTable] = None
dc_x = 0
dc_yl = 0
dc_yh = 0
dc_iscale: Fixed = 0
dc_texturemid: Fixed = 0
dc_source: list[int] = []


def draw_column():
    """
    Draw a column.

    A column is a vertical slice/span from a wall texture.

    This column will always have constant Z depth, given the
    DOOM style restrictions on view orientation.

    Thus a special case loop for very fast rendering can be used.
    It has also been used with Wolfenstein 3D.
    """
    count = dc_yh - dc_yl
    if count < 0:
        return

    if RANGECHECK and (dc_x >= SCREEN_WIDTH or dc_yl < 0 or dc_yh > SCREEN_HEIGHT):
        print(
            f"{draw_column.__qualname__}: {dc_yl} to {dc_yh} at {dc_x}", file=sys.stderr
        )
        exit(1)

    # TODO
    # dest = ylookup[dc_yl] + columnofs[dc_x]

    # fracstep = dc_iscale
    # frac = dc_texturemid + (dc_yl - centery) * fracstep

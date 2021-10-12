"""Nil."""

from enum import IntEnum, auto

from pink_doom.misc.fixed import Fixed


class BoxCoord(IntEnum):
    """Bounding box coordinate storage."""

    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()


def clear_box(box: list[Fixed]) -> None:
    """TODO."""


def add_to_box(box: list[Fixed], x: Fixed, y: Fixed) -> None:
    """TODO."""

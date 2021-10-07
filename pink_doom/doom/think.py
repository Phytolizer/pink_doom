"""
MapObj data.

Map Objects or mobjs are actors, entities, thinkers, take-your-pick...
anything that moves, acts, or suffers state changes of more or less violent nature.
"""
from dataclasses import dataclass
from typing import Callable

ActionFunction = Callable


@dataclass
class Thinker:
    """Actor."""

    function: ActionFunction

"""The Thinker class definition."""
from typing import Callable


class Thinker:
    """Holds a function that "thinks"."""

    function: Callable

    def __init__(self):
        """Create a Thinker."""
        self.function = None

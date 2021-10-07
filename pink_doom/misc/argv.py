"""Arguments handling."""
import sys

my_argc = 0
my_argv: list[str] = []


def check_parm(check: str) -> int:
    """
    Determine the location of a parameter in my_argv.

    Returns the position of the given parameter in the arg list (0 if not found).
    """
    for i, arg in enumerate(sys.argv[1:]):
        if arg.lower() == check.lower():
            return i
    return 0

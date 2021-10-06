"""Fixed point, 32bit as 16.16."""

from pink_doom.doom.types import MAX_INT, MIN_INT

FRAC_BITS = 16
FRAC_UNIT = 1 << FRAC_BITS


def fixed_mul(a, b):
    """Multiplies two fixed point numbers."""
    return (a * b) >> FRAC_BITS


def fixed_div(a, b):
    """Divides two fixed point numbers."""
    if (abs(a) >> 14) >= abs(b):
        if a ^ b < 0:
            return MIN_INT
        else:
            return MAX_INT
    else:
        return fixed_div2(a, b)


def fixed_div2(a, b):
    """Divides two fixed point numbers for case when we need to do floating point arithmetic."""
    c = a / b * FRAC_UNIT
    if c > MAX_INT or c < MIN_INT:
        raise ZeroDivisionError("FixedDiv: divide by zero")
    else:
        return int(c)

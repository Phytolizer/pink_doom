"""
All the global variables that store the internal state.

Theoretically speaking, the internal state of the engine
should be found by looking at the variables collected
here, and every relevant module will have to include
this header files.

In practice, things are a bit messy.
"""


no_monsters = False
"""checkparm of ``-nomonsters``"""
respawn_parm = False
"""checkparm of ``-respawn``"""
fast_parm = False
"""checkparm of ``-fast``"""

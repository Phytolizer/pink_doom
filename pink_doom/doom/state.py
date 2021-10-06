"""
All the global variables that store the internal state.

Theoretically speaking, the internal state of the engine
should be found by looking at the variables collected
here, and every relevant module will have to include
this header files.

In practice, things are a bit messy.
"""

from pink_doom.doom.defines import GameMission, GameMode, GameState, Language, Skill

from pink_doom.doom.player import Player, PlayerStatistics

from pink_doom.doom.data import MapThing



no_monsters = False
"""checkparm of ``-nomonsters``"""
respawn_parm = False
"""checkparm of ``-respawn``"""
fast_parm = False
"""checkparm of ``-fast``"""
dev_parm = False
"""DEBUG: launched with ``-devparm``"""

game_mode = GameMode.INDETERMINED
"""Identify IWAD as shareware, retail, etc."""
game_mission = GameMission.NONE

modified_game = False
"""Set if homebrew PWAD stuff has been added."""

language = Language.ENGLISH

# Selected skill type, map, etc.

# Defaults from menu, methinks.
start_skill = Skill.MEDIUM
start_episode = 0
start_map = 0
autostart = False

# Selected by user.
game_skill = Skill.HARD
game_episode = 0
game_map = 0
respawn_monsters = False
"""Nightmare mode flag, single player."""

# These are multiplied by 8.
sfx_volume = 0
"""Maximum volume for sound."""
music_volume = 0
"""Maximum volume for music."""

# FIXME is this necessary with pygame?
music_device = None
sfx_device = None
desired_music_device = None
desired_sfx_device = None

# Status flags for refresh.
status_bar_active = False
"""
Depending on view size -- no status bar?

Note that there is no way to disable the status bar explicitly.
"""

automap_active = False
"""Whether we are in AutoMap mode."""
menu_active = False
"""Whether the menu is overlayed."""
paused = False
"""Whether the game is paused."""

view_active = False
"""FIXME what's this?"""
no_drawers = False
"""Disable drawing entirely."""
no_blit = False
"""FIXME what's this?"""

# FIXME are these referring to a literal window?
view_window_x = 0
view_window_y = 0
view_height = 0
view_width = 0
scaled_view_width = 0

view_angle_offset = 0
"""
This one is related to the 3-screen display mode.

ANG90 = left side, ANG270 = right.
"""

# Scores, rating.
# Statistics on a given map, for intermission.
total_kills = 0
total_items = 0
total_secrets = 0

level_start_tic = 0
"""Gametic at level start."""
level_time = 0
"""Tics in-game for par."""

demo_playback = False
demo_recording = False

single_demo = False
"""Quit after playing a single demo (from command-line)."""

game_state = GameState.DEMO_SCREEN

#-----------------------------
#  Internal parameters, fixed.
#  These are set by the engine, and not changed
#  according to user inputs. Partly load from
#  WAD, partly set at startup time.

gametic = 0

player = Player()
"""Bookkeeping on players - state."""

player_in_game = False

player_start = MapThing()

world_map_info = PlayerStatistics()

maxammo = []
"""LUT of ammunition limits for each kind. This doubles with BackPack powerup item"""

# File handling stuff.
basedefault = ""
debugfile = None

precache = False
"""if true, load all graphics at level load"""

wipe_game_state = GameState.WIPE

mouse_sensitivity = 0

singletics = False
body_que_slot = 0

sky_flat_num = 0


"""Contains the main function."""
import sys
from os import getenv, path

from pink_doom.doom import state
from pink_doom.doom.defines import GameMode
from pink_doom.doom.strings import DEVDATA, DEVMAPS
from pink_doom.misc import argv
from pink_doom.misc.argv import check_parm, my_argc, my_argv

_wad_files = []
_wad_file = ""
_map_dir = ""
_base_default = ""


def _add_file(file):
    _wad_files.append(file)


def _identify_version():
    """
    Check version.

    Checks availability of IWAD files by name,
    to determine whether registered/commercial features
    should be executed (notably loading PWADs).
    """
    doom_wad_dir = getenv("DOOMWADDIR", ".")
    doom2wad = path.join(doom_wad_dir, "doom2.wad")
    doomuwad = path.join(doom_wad_dir, "doomu.wad")
    doomwad = path.join(doom_wad_dir, "doom.wad")
    doom1wad = path.join(doom_wad_dir, "doom1.wad")
    plutoniawad = path.join(doom_wad_dir, "plutonia.wad")
    tntwad = path.join(doom_wad_dir, "tnt.wad")
    home = getenv("HOME", ".")
    global _base_default
    _base_default = path.join(home, "/.doomrc")

    if check_parm("-shdev") > 0:
        state.game_mode = GameMode.SHAREWARE
        state.dev_parm = True
        _add_file(path.join(DEVDATA, "doom1.wad"))
        _add_file(path.join(DEVMAPS, "data_se", "texture1.lmp"))
        _add_file(path.join(DEVMAPS, "data_se", "pnames.lmp"))
        _base_default = path.join(DEVDATA, "default.cfg")
        return

    if check_parm("-regdev") > 0:
        state.game_mode = GameMode.REGISTERED
        state.dev_parm = True
        _add_file(path.join(DEVDATA, "doom.wad"))
        _add_file(path.join(DEVMAPS, "data_se", "texture1.lmp"))
        _add_file(path.join(DEVMAPS, "data_se", "texture2.lmp"))
        _add_file(path.join(DEVMAPS, "data_se", "pnames.lmp"))
        _base_default = path.join(DEVDATA, "default.cfg")
        return

    if check_parm("-comdev") > 0:
        state.game_mode = GameMode.COMMERCIAL
        state.dev_parm = True
        _add_file(path.join(DEVDATA, "doom2.wad"))
        _add_file(path.join(DEVMAPS, "cdata", "texture1.lmp"))
        _add_file(path.join(DEVMAPS, "cdata", "pnames.lmp"))
        _base_default = path.join(DEVDATA, "default.cfg")
        return

    if path.exists(doom2wad):
        state.game_mode = GameMode.COMMERCIAL
        _add_file(doom2wad)
        return

    if path.exists(plutoniawad):
        state.game_mode = GameMode.COMMERCIAL
        _add_file(plutoniawad)
        return

    if path.exists(tntwad):
        state.game_mode = GameMode.COMMERCIAL
        _add_file(tntwad)
        return

    if path.exists(doomuwad):
        state.game_mode = GameMode.RETAIL
        _add_file(doomuwad)
        return

    if path.exists(doomwad):
        state.game_mode = GameMode.REGISTERED
        _add_file(doomwad)
        return

    if path.exists(doom1wad):
        state.game_mode = GameMode.SHAREWARE
        _add_file(doom1wad)
        return

    print("Game mode indeterminate.")
    state.game_mode = GameMode.INDETERMINED


def _find_response_file():
    for i, arg in enumerate(my_argv[1:]):
        if arg.startswith("@"):
            try:
                with open(arg[1:], "rb") as handle:
                    print(f"Found response file {arg[1:]}!")
                    file = handle.read().decode("utf-8")
            except IOError:
                print("No such response file!", file=sys.stderr)
                exit(1)
            more_args = my_argv[i + 1 : my_argc]
            first_argv = my_argv[0]
            argv.my_argv = [first_argv, *file.split(), *more_args]
            argv.my_argc = len(my_argv)

            print(f"{my_argc} command-line args:")
            for a in my_argv[1:]:
                print(a)
            break


def main():
    """Begin running the entire application."""
    _find_response_file()
    _identify_version()

"""The Doom WAD reader."""
import struct
import sys
from dataclasses import dataclass
from io import SEEK_SET, FileIO
from os import fstat

import pink_doom.doom.state as state


@dataclass
class WadInfo:
    """The WAD header."""

    identification: str
    """Should be IWAD or PWAD."""
    num_lumps: int
    info_table_offset: int


@dataclass
class FileLump:
    """A single directory entry in the WAD."""

    file_pos: int
    size: int
    name: str


@dataclass
class LumpInfo:
    """Information about a lump in the ``lump_cache``."""

    handle: FileIO
    position: int
    size: int
    name: str


lump_cache = []
lump_info: list[LumpInfo] = []
num_lumps = 0


def _file_length(handle: int) -> int:
    return fstat(handle).st_size


def _add_file(name: str):
    file_info = b""
    try:
        with open(name, "rb") as f:
            print(f" adding {name}")
            global num_lumps, lump_info
            start_lump = num_lumps
            header_data = f.read(12)
            #                                 id, num_lumps, info_table_offset
            header = WadInfo(*struct.unpack("<4s  i          i", header_data))
            print(header)
            if header.identification not in (b"IWAD", b"PWAD"):
                print(f"Wad file {name} doesn't have IWAD or PWAD id", file=sys.stderr)
                exit(1)
            if header.identification == b"PWAD":
                state.modified_game = True
            # 16 == sizeof filelump_t
            length = header.num_lumps * 16
            f.seek(header.info_table_offset, SEEK_SET)
            file_info = f.read(length)
            num_lumps += header.num_lumps
            lump_info.extend(None for _ in range(header.num_lumps))
            for i in range(header.num_lumps):
                entry = file_info[i * 16 : (i + 1) * 16]
                lump_info[start_lump + i] = LumpInfo(
                    f,
                    *struct.unpack("<i i 8s", entry),
                )
                # convert ASCII zero-terminated string to Unicode string
                lump_info[start_lump + i].name = (
                    lump_info[start_lump + i].name.decode("utf-8").split("\x00")[0]
                )
                print(repr(lump_info[start_lump + i].name))
    except IOError:
        print(f" couldn't read {name}")


def init_multiple_files(filenames):
    """
    Initialize and read multiple WADs.

    Lump names can appear multiple times.
    The name searcher looks backwards, so a later file
    does override all earlier ones.
    """
    for filename in filenames:
        _add_file(filename)

    global num_lumps, lump_cache
    if num_lumps == 0:
        print(f"{init_multiple_files.__qualname__}: no files found", file=sys.stderr)
        exit(1)
    lump_cache = [None for _ in range(num_lumps)]


def check_num_for_name(name: str) -> int:
    """Return -1 if lump not found."""
    for i in range(num_lumps - 1, -1, -1):
        if lump_info[i].name == name:
            return i
    return -1


def get_num_for_name(name: str) -> int:
    """Crash if not found."""
    i = check_num_for_name(name)
    if i == -1:
        print(f"{get_num_for_name.__qualname__}: {name} not found", file=sys.stderr)
        exit(1)

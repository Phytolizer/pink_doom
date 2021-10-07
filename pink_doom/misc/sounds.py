"""DOOM sound info."""
from dataclasses import dataclass
from enum import Enum, auto


class MusicEnum(Enum):
    """Identifiers for all music."""

    NONE = auto()
    E1M1 = auto()
    E1M2 = auto()
    E1M3 = auto()
    E1M4 = auto()
    E1M5 = auto()
    E1M6 = auto()
    E1M7 = auto()
    E1M8 = auto()
    E1M9 = auto()
    E2M1 = auto()
    E2M2 = auto()
    E2M3 = auto()
    E2M4 = auto()
    E2M5 = auto()
    E2M6 = auto()
    E2M7 = auto()
    E2M8 = auto()
    E2M9 = auto()
    E3M1 = auto()
    E3M2 = auto()
    E3M3 = auto()
    E3M4 = auto()
    E3M5 = auto()
    E3M6 = auto()
    E3M7 = auto()
    E3M8 = auto()
    E3M9 = auto()
    INTER = auto()
    INTRO = auto()
    BUNNY = auto()
    VICTOR = auto()
    INTROA = auto()
    RUNNIN = auto()
    STALKS = auto()
    COUNTD = auto()
    BETWEE = auto()
    DOOM = auto()
    THE_DA = auto()
    SHAWN = auto()
    DDTBLU = auto()
    IN_CIT = auto()
    DEAD = auto()
    STLKS2 = auto()
    THEDA2 = auto()
    DOOM2 = auto()
    DDTBL2 = auto()
    RUNNI2 = auto()
    DEAD2 = auto()
    STLKS3 = auto()
    ROMERO = auto()
    SHAWN2 = auto()
    MESSAG = auto()
    COUNT2 = auto()
    DDTBL3 = auto()
    AMPIE = auto()
    THEDA3 = auto()
    ADRIAN = auto()
    MESSG2 = auto()
    ROMER2 = auto()
    TENSE = auto()
    SHAWN3 = auto()
    OPENIN = auto()
    EVIL = auto()
    ULTIMA = auto()
    READ_M = auto()
    DM2TTL = auto()
    DM2INT = auto()
    NUM_MUSIC = auto()


class SfxEnum(Enum):
    """Identifiers for all sfx in game."""

    NONE = auto()
    PISTOL = auto()
    SHOTGN = auto()
    SGCOCK = auto()
    DSHTGN = auto()
    DBOPN = auto()
    DBCLS = auto()
    DBLOAD = auto()
    PLASMA = auto()
    BFG = auto()
    SAWUP = auto()
    SAWIDL = auto()
    SAWFUL = auto()
    SAWHIT = auto()
    RLAUNC = auto()
    RXPLOD = auto()
    FIRSHT = auto()
    FIRXPL = auto()
    PSTART = auto()
    PSTOP = auto()
    DOROPN = auto()
    DORCLS = auto()
    STNMOV = auto()
    SWTCHN = auto()
    SWTCHX = auto()
    PLPAIN = auto()
    DMPAIN = auto()
    POPAIN = auto()
    VIPAIN = auto()
    MNPAIN = auto()
    PEPAIN = auto()
    SLOP = auto()
    ITEMUP = auto()
    WPNUP = auto()
    OOF = auto()
    TELEPT = auto()
    POSIT1 = auto()
    POSIT2 = auto()
    POSIT3 = auto()
    BGSIT1 = auto()
    BGSIT2 = auto()
    SGTSIT = auto()
    CACSIT = auto()
    BRSSIT = auto()
    CYBSIT = auto()
    SPISIT = auto()
    BSPSIT = auto()
    KNTSIT = auto()
    VILSIT = auto()
    MANSIT = auto()
    PESIT = auto()
    SKLATK = auto()
    SGTATK = auto()
    SKEPCH = auto()
    VILATK = auto()
    CLAW = auto()
    SKESWG = auto()
    PLDETH = auto()
    PDIEHI = auto()
    PODTH1 = auto()
    PODTH2 = auto()
    PODTH3 = auto()
    BGDTH1 = auto()
    BGDTH2 = auto()
    SGTDTH = auto()
    CACDTH = auto()
    SKLDTH = auto()
    BRSDTH = auto()
    CYBDTH = auto()
    SPIDTH = auto()
    BSPDTH = auto()
    VILDTH = auto()
    KNTDTH = auto()
    PEDTH = auto()
    SKEDTH = auto()
    POSACT = auto()
    BGACT = auto()
    DMACT = auto()
    BSPACT = auto()
    BSPWLK = auto()
    VILACT = auto()
    NOWAY = auto()
    BAREXP = auto()
    PUNCH = auto()
    HOOF = auto()
    METAL = auto()
    CHGUN = auto()
    TINK = auto()
    BDOPN = auto()
    BDCLS = auto()
    ITMBK = auto()
    FLAME = auto()
    FLAMST = auto()
    GETPOW = auto()
    BOSPIT = auto()
    BOSCUB = auto()
    BOSSIT = auto()
    BOSPN = auto()
    BOSDTH = auto()
    MANATK = auto()
    MANDTH = auto()
    SSSIT = auto()
    SSDTH = auto()
    KEENPN = auto()
    KEENDT = auto()
    SKEACT = auto()
    SKESIT = auto()
    SKEATK = auto()
    RADIO = auto()
    NUM_SFX = auto()


@dataclass
class SfxInfo:
    """SoundFX struct."""

    name: str
    """up to 6-character name"""
    singularity: bool
    """Sfx singularity (only one at a time)"""
    priority: int
    """Sfx priority"""
    link: SfxEnum
    """referenced sound if a link"""
    pitch: int
    """pitch if a link"""
    volume: int
    """volume if a link"""
    data: bytes = b""
    """sound data"""
    usefulness: int = 0
    """
    Sound usefulness.

    This is checked every second to see if the sound
    can be thrown out (if 0, then decrement, if -1,
    then throw out, if > 0, then it is in use)
    """
    lump_num: int = 0
    """lump number of sfx"""


@dataclass
class MusicInfo:
    """MusicInfo struct."""

    name: str
    """up to 6-character name"""
    lump_num: int = 0
    """lump number of music"""
    data: bytes = b""
    """music data"""
    handle: int = 0
    """music handle once registered"""


music = (
    MusicInfo("", 0),
    MusicInfo("e1m1", 0),
    MusicInfo("e1m2", 0),
    MusicInfo("e1m3", 0),
    MusicInfo("e1m4", 0),
    MusicInfo("e1m5", 0),
    MusicInfo("e1m6", 0),
    MusicInfo("e1m7", 0),
    MusicInfo("e1m8", 0),
    MusicInfo("e1m9", 0),
    MusicInfo("e2m1", 0),
    MusicInfo("e2m2", 0),
    MusicInfo("e2m3", 0),
    MusicInfo("e2m4", 0),
    MusicInfo("e2m5", 0),
    MusicInfo("e2m6", 0),
    MusicInfo("e2m7", 0),
    MusicInfo("e2m8", 0),
    MusicInfo("e2m9", 0),
    MusicInfo("e3m1", 0),
    MusicInfo("e3m2", 0),
    MusicInfo("e3m3", 0),
    MusicInfo("e3m4", 0),
    MusicInfo("e3m5", 0),
    MusicInfo("e3m6", 0),
    MusicInfo("e3m7", 0),
    MusicInfo("e3m8", 0),
    MusicInfo("e3m9", 0),
    MusicInfo("inter", 0),
    MusicInfo("intro", 0),
    MusicInfo("bunny", 0),
    MusicInfo("victor", 0),
    MusicInfo("introa", 0),
    MusicInfo("runnin", 0),
    MusicInfo("stalks", 0),
    MusicInfo("countd", 0),
    MusicInfo("betwee", 0),
    MusicInfo("doom", 0),
    MusicInfo("the_da", 0),
    MusicInfo("shawn", 0),
    MusicInfo("ddtblu", 0),
    MusicInfo("in_cit", 0),
    MusicInfo("dead", 0),
    MusicInfo("stlks2", 0),
    MusicInfo("theda2", 0),
    MusicInfo("doom2", 0),
    MusicInfo("ddtbl2", 0),
    MusicInfo("runni2", 0),
    MusicInfo("dead2", 0),
    MusicInfo("stlks3", 0),
    MusicInfo("romero", 0),
    MusicInfo("shawn2", 0),
    MusicInfo("messag", 0),
    MusicInfo("count2", 0),
    MusicInfo("ddtbl3", 0),
    MusicInfo("ampie", 0),
    MusicInfo("theda3", 0),
    MusicInfo("adrian", 0),
    MusicInfo("messg2", 0),
    MusicInfo("romer2", 0),
    MusicInfo("tense", 0),
    MusicInfo("shawn3", 0),
    MusicInfo("openin", 0),
    MusicInfo("evil", 0),
    MusicInfo("ultima", 0),
    MusicInfo("read_m", 0),
    MusicInfo("dm2ttl", 0),
    MusicInfo("dm2int", 0),
)

sfx = (
    SfxInfo("none", False, 0, SfxEnum.NONE, -1, -1),
    SfxInfo("pistol", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("shotgn", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("sgcock", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("dshtgn", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("dbopn", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("dbcls", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("dbload", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("plasma", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("bfg", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("sawup", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("sawidl", False, 118, SfxEnum.NONE, -1, -1),
    SfxInfo("sawful", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("sawhit", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("rlaunc", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("rxplod", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("firsht", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("firxpl", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("pstart", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("pstop", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("doropn", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("dorcls", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("stnmov", False, 119, SfxEnum.NONE, -1, -1),
    SfxInfo("swtchn", False, 78, SfxEnum.NONE, -1, -1),
    SfxInfo("swtchx", False, 78, SfxEnum.NONE, -1, -1),
    SfxInfo("plpain", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("dmpain", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("popain", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("vipain", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("mnpain", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("pepain", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("slop", False, 78, SfxEnum.NONE, -1, -1),
    SfxInfo("itemup", True, 78, SfxEnum.NONE, -1, -1),
    SfxInfo("wpnup", True, 78, SfxEnum.NONE, -1, -1),
    SfxInfo("oof", False, 96, SfxEnum.NONE, -1, -1),
    SfxInfo("telept", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("posit1", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("posit2", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("posit3", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("bgsit1", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("bgsit2", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("sgtsit", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("cacsit", True, 98, SfxEnum.NONE, -1, -1),
    SfxInfo("brssit", True, 94, SfxEnum.NONE, -1, -1),
    SfxInfo("cybsit", True, 92, SfxEnum.NONE, -1, -1),
    SfxInfo("spisit", True, 90, SfxEnum.NONE, -1, -1),
    SfxInfo("bspsit", True, 90, SfxEnum.NONE, -1, -1),
    SfxInfo("kntsit", True, 90, SfxEnum.NONE, -1, -1),
    SfxInfo("vilsit", True, 90, SfxEnum.NONE, -1, -1),
    SfxInfo("mansit", True, 90, SfxEnum.NONE, -1, -1),
    SfxInfo("pesit", True, 90, SfxEnum.NONE, -1, -1),
    SfxInfo("sklatk", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("sgtatk", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("skepch", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("vilatk", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("claw", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("skeswg", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("pldeth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("pdiehi", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("podth1", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("podth2", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("podth3", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("bgdth1", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("bgdth2", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("sgtdth", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("cacdth", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("skldth", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("brsdth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("cybdth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("spidth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("bspdth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("vildth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("kntdth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("pedth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("skedth", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("posact", True, 120, SfxEnum.NONE, -1, -1),
    SfxInfo("bgact", True, 120, SfxEnum.NONE, -1, -1),
    SfxInfo("dmact", True, 120, SfxEnum.NONE, -1, -1),
    SfxInfo("bspact", True, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("bspwlk", True, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("vilact", True, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("noway", False, 78, SfxEnum.NONE, -1, -1),
    SfxInfo("barexp", False, 60, SfxEnum.NONE, -1, -1),
    SfxInfo("punch", False, 64, SfxEnum.NONE, -1, -1),
    SfxInfo("hoof", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("metal", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("chgun", False, 64, SfxEnum.PISTOL, 150, 0),
    SfxInfo("tink", False, 60, SfxEnum.NONE, -1, -1),
    SfxInfo("bdopn", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("bdcls", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("itmbk", False, 100, SfxEnum.NONE, -1, -1),
    SfxInfo("flame", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("flamst", False, 32, SfxEnum.NONE, -1, -1),
    SfxInfo("getpow", False, 60, SfxEnum.NONE, -1, -1),
    SfxInfo("bospit", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("boscub", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("bossit", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("bospn", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("bosdth", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("manatk", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("mandth", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("sssit", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("ssdth", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("keenpn", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("keendt", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("skeact", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("skesit", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("skeatk", False, 70, SfxEnum.NONE, -1, -1),
    SfxInfo("radio", False, 60, SfxEnum.NONE, -1, -1),
)

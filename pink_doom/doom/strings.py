"""Printed strings for translation."""

# pink_doom/doom/main.py
DEV_STR = "Development mode ON.\n"
CDROM = "CD-ROM Version: default.cfg from c:\\doomdata\n"

# pink_doom/misc/menu.py
PRESS_KEY = "press a key."
PRESS_YN = "press y or n."
QUIT_MSG = "are you sure you want to\nquit this great game?"
QSAVE_SPOT = "you haven't picked a quicksave slot yet!\n\n" + PRESS_KEY
SAVE_DEAD = "you can't save if you aren't playing!\n\n" + PRESS_KEY
QSPROMPT = "quicksave over your game named\n\n'{}'?\n\n" + PRESS_YN
QLPROMPT = "do you want to quickload the game named\n\n'{}'?" + PRESS_YN

NIGHTMARE = (
    "are you sure? this skill level\n" + "isn't even remotely fair.\n\n" + PRESS_YN
)
SW_STRING = (
    "this is the shareware version of doom.\n\n"
    + "you need to order the entire trilogy.\n\n"
    + PRESS_KEY
)

MSG_OFF = "Messages OFF"
MSG_ON = "Messages ON"
END_GAME = "are you sure you want to end the game?\n\n" + PRESS_YN

DOS_Y = "(press y to quit)"

DETAIL_HI = "High detail"
DETAIL_LO = "Low detail"
GAMMA_LVL_0 = "Gamma correction OFF"
GAMMA_LVL_1 = "Gamma correction level 1"
GAMMA_LVL_2 = "Gamma correction level 2"
GAMMA_LVL_3 = "Gamma correction level 3"
GAMMA_LVL_4 = "Gamma correction level 4"
EMPTY_STRING = "empty slot"

# pink_doom/playsim/interactions.py
GOT_ARMOR = "Picked up the armor."
GOT_MEGA = "Picked up the MegaArmor!"
GOT_HTH_BONUS = "Picked up a health bonus."
GOT_ARM_BONUS = "Picked up an armor bonus."
GOT_STIM = "Picked up a stimpack."
GOT_MEDI_NEED = "Picked up a medikit that you REALLY need!"
GOT_MEDIKIT = "Picked up a medikit."
GOT_SUPER = "Supercharge!"

GOT_BLUE_CARD = "Picked up a blue keycard."
GOT_YELW_CARD = "Picked up a yellow keycard."
GOT_RED_CARD = "Picked up a red keycard."
GOT_BLUE_SKUL = "Picked up a blue skull key."
GOT_YELW_SKUL = "Picked up a yellow skull key."
GOT_RED_SKUL = "Picked up a red skull key."

GOT_INVUL = "Invulnerability!"
GOT_BERSERK = "Berserk!"
GOT_INVIS = "Partial Invisibility"
GOT_SUIT = "Radiation Shielding Suit"
GOT_MAP = "Computer Area Map"
GOT_VISOR = "Light Amplification Visor"
GOT_MSPHERE = "MegaSphere!"

GOTCLIP = "Picked up a clip."
GOTCLIPBOX = "Picked up a box of bullets."
GOTROCKET = "Picked up a rocket."
GOTROCKBOX = "Picked up a box of rockets."
GOTCELL = "Picked up an energy cell."
GOTCELLBOX = "Picked up an energy cell pack."
GOTSHELLS = "Picked up 4 shotgun shells."
GOTSHELLBOX = "Picked up a box of shotgun shells."
GOTBACKPACK = "Picked up a backpack full of ammo!"

GOTBFG9000 = "You got the BFG9000!  Oh, yes."
GOTCHAINGUN = "You got the chaingun!"
GOTCHAINSAW = "A chainsaw!  Find some meat!"
GOTLAUNCHER = "You got the rocket launcher!"
GOTPLASMA = "You got the plasma gun!"
GOTSHOTGUN = "You got the shotgun!"
GOTSHOTGUN2 = "You got the super shotgun!"

# pink_doom/playsim/doors.py
BLUE_KEY_OBJ = "You need a blue key to activate this object"
RED_KEY_OBJ = "You need a red key to activate this object"
YELLOW_KEY_OBJ = "You need a yellow key to activate this object"
BLUE_KEY_DOOR = "You need a blue key to open this door"
RED_KEY_DOOR = "You need a red key to open this door"
YELLOW_KEY_DOOR = "You need a yellow key to open this door"

# pink_doom/game/game.py
GAME_SAVED = "game saved."

# pink_doom/hud/stuff.py
HUSTR_MSGU = "[Message unsent]"

HUSTR_E1M1 = "E1M1: Hangar"
HUSTR_E1M2 = "E1M2: Nuclear Plant"
HUSTR_E1M3 = "E1M3: Toxin Refinery"
HUSTR_E1M4 = "E1M4: Command Control"
HUSTR_E1M5 = "E1M5: Phobos Lab"
HUSTR_E1M6 = "E1M6: Central Processing"
HUSTR_E1M7 = "E1M7: Computer Station"
HUSTR_E1M8 = "E1M8: Phobos Anomaly"
HUSTR_E1M9 = "E1M9: Military Base"

HUSTR_E2M1 = "E2M1: Deimos Anomaly"
HUSTR_E2M2 = "E2M2: Containment Area"
HUSTR_E2M3 = "E2M3: Refinery"
HUSTR_E2M4 = "E2M4: Deimos Lab"
HUSTR_E2M5 = "E2M5: Command Center"
HUSTR_E2M6 = "E2M6: Halls of the Damned"
HUSTR_E2M7 = "E2M7: Spawning Vats"
HUSTR_E2M8 = "E2M8: Tower of Babel"
HUSTR_E2M9 = "E2M9: Fortress of Mystery"

HUSTR_E3M1 = "E3M1: Hell Keep"
HUSTR_E3M2 = "E3M2: Slough of Despair"
HUSTR_E3M3 = "E3M3: Pandemonium"
HUSTR_E3M4 = "E3M4: House of Pain"
HUSTR_E3M5 = "E3M5: Unholy Cathedral"
HUSTR_E3M6 = "E3M6: Mt. Erebus"
HUSTR_E3M7 = "E3M7: Limbo"
HUSTR_E3M8 = "E3M8: Dis"
HUSTR_E3M9 = "E3M9: Warrens"

HUSTR_E4M1 = "E4M1: Hell Beneath"
HUSTR_E4M2 = "E4M2: Perfect Hatred"
HUSTR_E4M3 = "E4M3: Sever The Wicked"
HUSTR_E4M4 = "E4M4: Unruly Evil"
HUSTR_E4M5 = "E4M5: They Will Repent"
HUSTR_E4M6 = "E4M6: Against Thee Wickedly"
HUSTR_E4M7 = "E4M7: And Hell Followed"
HUSTR_E4M8 = "E4M8: Unto The Cruel"
HUSTR_E4M9 = "E4M9: Fear"

HUSTR_1 = "level 1: entryway"
HUSTR_2 = "level 2: underhalls"
HUSTR_3 = "level 3: the gantlet"
HUSTR_4 = "level 4: the focus"
HUSTR_5 = "level 5: the waste tunnels"
HUSTR_6 = "level 6: the crusher"
HUSTR_7 = "level 7: dead simple"
HUSTR_8 = "level 8: tricks and traps"
HUSTR_9 = "level 9: the pit"
HUSTR_10 = "level 10: refueling base"
HUSTR_11 = "level 11: 'o' of destruction!"

HUSTR_12 = "level 12: the factory"
HUSTR_13 = "level 13: downtown"
HUSTR_14 = "level 14: the inmost dens"
HUSTR_15 = "level 15: industrial zone"
HUSTR_16 = "level 16: suburbs"
HUSTR_17 = "level 17: tenements"
HUSTR_18 = "level 18: the courtyard"
HUSTR_19 = "level 19: the citadel"
HUSTR_20 = "level 20: gotcha!"

HUSTR_21 = "level 21: nirvana"
HUSTR_22 = "level 22: the catacombs"
HUSTR_23 = "level 23: barrels o' fun"
HUSTR_24 = "level 24: the chasm"
HUSTR_25 = "level 25: bloodfalls"
HUSTR_26 = "level 26: the abandoned mines"
HUSTR_27 = "level 27: monster condo"
HUSTR_28 = "level 28: the spirit world"
HUSTR_29 = "level 29: the living end"
HUSTR_30 = "level 30: icon of sin"

HUSTR_31 = "level 31: wolfenstein"
HUSTR_32 = "level 32: grosse"

PHUSTR_1 = "level 1: congo"
PHUSTR_2 = "level 2: well of souls"
PHUSTR_3 = "level 3: aztec"
PHUSTR_4 = "level 4: caged"
PHUSTR_5 = "level 5: ghost town"
PHUSTR_6 = "level 6: baron's lair"
PHUSTR_7 = "level 7: caughtyard"
PHUSTR_8 = "level 8: realm"
PHUSTR_9 = "level 9: abattoire"
PHUSTR_10 = "level 10: onslaught"
PHUSTR_11 = "level 11: hunted"

PHUSTR_12 = "level 12: speed"
PHUSTR_13 = "level 13: the crypt"
PHUSTR_14 = "level 14: genesis"
PHUSTR_15 = "level 15: the twilight"
PHUSTR_16 = "level 16: the omen"
PHUSTR_17 = "level 17: compound"
PHUSTR_18 = "level 18: neurosphere"
PHUSTR_19 = "level 19: nme"
PHUSTR_20 = "level 20: the death domain"

PHUSTR_21 = "level 21: slayer"
PHUSTR_22 = "level 22: impossible mission"
PHUSTR_23 = "level 23: tombstone"
PHUSTR_24 = "level 24: the final frontier"
PHUSTR_25 = "level 25: the temple of darkness"
PHUSTR_26 = "level 26: bunker"
PHUSTR_27 = "level 27: anti-christ"
PHUSTR_28 = "level 28: the sewers"
PHUSTR_29 = "level 29: odyssey of noises"
PHUSTR_30 = "level 30: the gateway of hell"

PHUSTR_31 = "level 31: cyberden"
PHUSTR_32 = "level 32: go 2 it"

THUSTR_1 = "level 1: system control"
THUSTR_2 = "level 2: human bbq"
THUSTR_3 = "level 3: power control"
THUSTR_4 = "level 4: wormhole"
THUSTR_5 = "level 5: hanger"
THUSTR_6 = "level 6: open season"
THUSTR_7 = "level 7: prison"
THUSTR_8 = "level 8: metal"
THUSTR_9 = "level 9: stronghold"
THUSTR_10 = "level 10: redemption"
THUSTR_11 = "level 11: storage facility"

THUSTR_12 = "level 12: crater"
THUSTR_13 = "level 13: nukage processing"
THUSTR_14 = "level 14: steel works"
THUSTR_15 = "level 15: dead zone"
THUSTR_16 = "level 16: deepest reaches"
THUSTR_17 = "level 17: processing area"
THUSTR_18 = "level 18: mill"
THUSTR_19 = "level 19: shipping/respawning"
THUSTR_20 = "level 20: central processing"

THUSTR_21 = "level 21: administration center"
THUSTR_22 = "level 22: habitat"
THUSTR_23 = "level 23: lunar mining project"
THUSTR_24 = "level 24: quarry"
THUSTR_25 = "level 25: baron's den"
THUSTR_26 = "level 26: ballistyx"
THUSTR_27 = "level 27: mount pain"
THUSTR_28 = "level 28: heck"
THUSTR_29 = "level 29: river styx"
THUSTR_30 = "level 30: last call"

THUSTR_31 = "level 31: pharaoh"
THUSTR_32 = "level 32: caribbean"

# pink_doom/automap/map.py
AMSTR_FOLLOWON = "Follow Mode ON"
AMSTR_FOLLOWOFF = "Follow Mode OFF"

AMSTR_GRIDON = "Grid ON"
AMSTR_GRIDOFF = "Grid OFF"

AMSTR_MARKEDSPOT = "Marked Spot"
AMSTR_MARKSCLEARED = "All Marks Cleared"

# pink_doom/stuff/stuff.c
STSTR_MUS = "Music Change"
STSTR_NOMUS = "IMPOSSIBLE SELECTION"
STSTR_DQDON = "Degreelessness Mode On"
STSTR_DQDOFF = "Degreelessness Mode Off"

STSTR_KFAADDED = "Very Happy Ammo Added"
STSTR_FAADDED = "Ammo (no keys) Added"

STSTR_NCON = "No Clipping Mode ON"
STSTR_NCOFF = "No Clipping Mode OFF"

STSTR_BEHOLD = "inVuln, Str, Inviso, Rad, Allmap, or Lite-amp"
STSTR_BEHOLDX = "Power-up Toggled"

STSTR_CHOPPERS = "... doesn't suck - GM"
STSTR_CLEV = "Changing Level..."

# pink_doom/finale/finale.py
E1TEXT = (
    "Once you beat the big badasses and\n"
    "clean out the moon base you're supposed\n"
    "to win, aren't you? Aren't you? Where's\n"
    "your fat reward and ticket home? What\n"
    "the hell is this? It's not supposed to\n"
    "end this way!\n"
    "\n"
    "It stinks like rotten meat, but looks\n"
    "like the lost Deimos base.  Looks like\n"
    "you're stuck on The Shores of Hell.\n"
    "The only way out is through.\n"
    "\n"
    "To continue the DOOM experience, play\n"
    "The Shores of Hell and its amazing\n"
    "sequel, Inferno!\n"
)

E2TEXT = (
    "You've done it! The hideous cyber-\n"
    "demon lord that ruled the lost Deimos\n"
    "moon base has been slain and you\n"
    "are triumphant! But ... where are\n"
    "you? You clamber to the edge of the\n"
    "moon and look down to see the awful\n"
    "truth.\n"
    "\n"
    "Deimos floats above Hell itself!\n"
    "You've never heard of anyone escaping\n"
    "from Hell, but you'll make the bastards\n"
    "sorry they ever heard of you! Quickly,\n"
    "you rappel down to  the surface of\n"
    "Hell.\n"
    "\n"
    "Now, it's on to the final chapter of\n"
    "DOOM! -- Inferno."
)

E3TEXT = (
    "The loathsome spiderdemon that\n"
    "masterminded the invasion of the moon\n"
    "bases and caused so much death has had\n"
    "its ass kicked for all time.\n"
    "\n"
    "A hidden doorway opens and you enter.\n"
    "You've proven too tough for Hell to\n"
    "contain, and now Hell at last plays\n"
    "fair -- for you emerge from the door\n"
    "to see the green fields of Earth!\n"
    "Home at last.\n"
    "\n"
    "You wonder what's been happening on\n"
    "Earth while you were battling evil\n"
    "unleashed. It's good that no Hell-\n"
    "spawn could have come through that\n"
    "door with you ..."
)

E4TEXT = (
    "the spider mastermind must have sent forth\n"
    "its legions of hellspawn before your\n"
    "final confrontation with that terrible\n"
    "beast from hell.  but you stepped forward\n"
    "and brought forth eternal damnation and\n"
    "suffering upon the horde as a true hero\n"
    "would in the face of something so evil.\n"
    "\n"
    "besides, someone was gonna pay for what\n"
    "happened to daisy, your pet rabbit.\n"
    "\n"
    "but now, you see spread before you more\n"
    "potential pain and gibbitude as a nation\n"
    "of demons run amok among our cities.\n"
    "\n"
    "next stop, hell on earth!"
)

# after level 6, put this:

C1TEXT = (
    "YOU HAVE ENTERED DEEPLY INTO THE INFESTED\n"
    "STARPORT. BUT SOMETHING IS WRONG. THE\n"
    "MONSTERS HAVE BROUGHT THEIR OWN REALITY\n"
    "WITH THEM, AND THE STARPORT'S TECHNOLOGY\n"
    "IS BEING SUBVERTED BY THEIR PRESENCE.\n"
    "\n"
    "AHEAD, YOU SEE AN OUTPOST OF HELL, A\n"
    "FORTIFIED ZONE. IF YOU CAN GET PAST IT,\n"
    "YOU CAN PENETRATE INTO THE HAUNTED HEART\n"
    "OF THE STARBASE AND FIND THE CONTROLLING\n"
    "SWITCH WHICH HOLDS EARTH'S POPULATION\n"
    "HOSTAGE."
)

# After level 11, put this:

C2TEXT = (
    "YOU HAVE WON! YOUR VICTORY HAS ENABLED\n"
    "HUMANKIND TO EVACUATE EARTH AND ESCAPE\n"
    "THE NIGHTMARE.  NOW YOU ARE THE ONLY\n"
    "HUMAN LEFT ON THE FACE OF THE PLANET.\n"
    "CANNIBAL MUTATIONS, CARNIVOROUS ALIENS,\n"
    "AND EVIL SPIRITS ARE YOUR ONLY NEIGHBORS.\n"
    "YOU SIT BACK AND WAIT FOR DEATH, CONTENT\n"
    "THAT YOU HAVE SAVED YOUR SPECIES.\n"
    "\n"
    "BUT THEN, EARTH CONTROL BEAMS DOWN A\n"
    'MESSAGE FROM SPACE: "SENSORS HAVE LOCATED\n'
    "THE SOURCE OF THE ALIEN INVASION. IF YOU\n"
    "GO THERE, YOU MAY BE ABLE TO BLOCK THEIR\n"
    "ENTRY.  THE ALIEN BASE IS IN THE HEART OF\n"
    "YOUR OWN HOME CITY, NOT FAR FROM THE\n"
    'STARPORT." SLOWLY AND PAINFULLY YOU GET\n'
    "UP AND RETURN TO THE FRAY."
)

# After level 20, put this:

C3TEXT = (
    "YOU ARE AT THE CORRUPT HEART OF THE CITY,\n"
    "SURROUNDED BY THE CORPSES OF YOUR ENEMIES.\n"
    "YOU SEE NO WAY TO DESTROY THE CREATURES'\n"
    "ENTRYWAY ON THIS SIDE, SO YOU CLENCH YOUR\n"
    "TEETH AND PLUNGE THROUGH IT.\n"
    "\n"
    "THERE MUST BE A WAY TO CLOSE IT ON THE\n"
    "OTHER SIDE. WHAT DO YOU CARE IF YOU'VE\n"
    "GOT TO GO THROUGH HELL TO GET TO IT?"
)

# After level 29, put this:

C4TEXT = (
    "THE HORRENDOUS VISAGE OF THE BIGGEST\n"
    "DEMON YOU'VE EVER SEEN CRUMBLES BEFORE\n"
    "YOU, AFTER YOU PUMP YOUR ROCKETS INTO\n"
    "HIS EXPOSED BRAIN. THE MONSTER SHRIVELS\n"
    "UP AND DIES, ITS THRASHING LIMBS\n"
    "DEVASTATING UNTOLD MILES OF HELL'S\n"
    "SURFACE.\n"
    "\n"
    "YOU'VE DONE IT. THE INVASION IS OVER.\n"
    "EARTH IS SAVED. HELL IS A WRECK. YOU\n"
    "WONDER WHERE BAD FOLKS WILL GO WHEN THEY\n"
    "DIE, NOW. WIPING THE SWEAT FROM YOUR\n"
    "FOREHEAD YOU BEGIN THE LONG TREK BACK\n"
    "HOME. REBUILDING EARTH OUGHT TO BE A\n"
    "LOT MORE FUN THAN RUINING IT WAS.\n"
)

# Before level 31, put this:

C5TEXT = (
    "CONGRATULATIONS, YOU'VE FOUND THE SECRET\n"
    "LEVEL! LOOKS LIKE IT'S BEEN BUILT BY\n"
    "HUMANS, RATHER THAN DEMONS. YOU WONDER\n"
    "WHO THE INMATES OF THIS CORNER OF HELL\n"
    "WILL BE."
)

# Before level 32, put this:

C6TEXT = (
    "CONGRATULATIONS, YOU'VE FOUND THE\n"
    "SUPER SECRET LEVEL!  YOU'D BETTER\n"
    "BLAZE THROUGH THIS ONE!\n"
)

# after map 06

P1TEXT = (
    "You gloat over the steaming carcass of the\n"
    "Guardian.  With its death, you've wrested\n"
    "the Accelerator from the stinking claws\n"
    "of Hell.  You relax and glance around the\n"
    "room.  Damn!  There was supposed to be at\n"
    "least one working prototype, but you can't\n"
    "see it. The demons must have taken it.\n"
    "\n"
    "You must find the prototype, or all your\n"
    "struggles will have been wasted. Keep\n"
    "moving, keep fighting, keep killing.\n"
    "Oh yes, keep living, too."
)

# after map 11

P2TEXT = (
    "Even the deadly Arch-Vile labyrinth could\n"
    "not stop you, and you've gotten to the\n"
    "prototype Accelerator which is soon\n"
    "efficiently and permanently deactivated.\n"
    "\n"
    "You're good at that kind of thing."
)

# after map 20

P3TEXT = (
    "You've bashed and battered your way into\n"
    "the heart of the devil-hive.  Time for a\n"
    "Search-and-Destroy mission, aimed at the\n"
    "Gatekeeper, whose foul offspring is\n"
    "cascading to Earth.  Yeah, he's bad. But\n"
    "you know who's worse!\n"
    "\n"
    "Grinning evilly, you check your gear, and\n"
    "get ready to give the bastard a little Hell\n"
    "of your own making!"
)

# after map 30

P4TEXT = (
    "The Gatekeeper's evil face is splattered\n"
    "all over the place.  As its tattered corpse\n"
    "collapses, an inverted Gate forms and\n"
    "sucks down the shards of the last\n"
    "prototype Accelerator, not to mention the\n"
    "few remaining demons.  You're done. Hell\n"
    "has gone back to pounding bad dead folks \n"
    "instead of good live ones.  Remember to\n"
    "tell your grandkids to put a rocket\n"
    "launcher in your coffin. If you go to Hell\n"
    "when you die, you'll need it for some\n"
    "final cleaning-up ..."
)

# before map 31

P5TEXT = (
    "You've found the second-hardest level we\n"
    "got. Hope you have a saved game a level or\n"
    "two previous.  If not, be prepared to die\n"
    "aplenty. For master marines only."
)

# before map 32

P6TEXT = (
    "Betcha wondered just what WAS the hardest\n"
    "level we had ready for ya?  Now you know.\n"
    "No one gets out alive."
)

T1TEXT = (
    "You've fought your way out of the infested\n"
    "experimental labs.   It seems that UAC has\n"
    "once again gulped it down.  With their\n"
    "high turnover, it must be hard for poor\n"
    "old UAC to buy corporate health insurance\n"
    "nowadays..\n"
    "\n"
    "Ahead lies the military complex, now\n"
    "swarming with diseased horrors hot to get\n"
    "their teeth into you. With luck, the\n"
    "complex still has some warlike ordnance\n"
    "laying around."
)

T2TEXT = (
    "You hear the grinding of heavy machinery\n"
    "ahead.  You sure hope they're not stamping\n"
    "out new hellspawn, but you're ready to\n"
    "ream out a whole herd if you have to.\n"
    "They might be planning a blood feast, but\n"
    "you feel about as mean as two thousand\n"
    "maniacs packed into one mad killer.\n"
    "\n"
    "You don't plan to go down easy."
)

T3TEXT = (
    "The vista opening ahead looks real damn\n"
    "familiar. Smells familiar, too -- like\n"
    "fried excrement. You didn't like this\n"
    "place before, and you sure as hell ain't\n"
    "planning to like it now. The more you\n"
    "brood on it, the madder you get.\n"
    "Hefting your gun, an evil grin trickles\n"
    "onto your face. Time to take some names."
)

T4TEXT = (
    "Suddenly, all is silent, from one horizon\n"
    "to the other. The agonizing echo of Hell\n"
    "fades away, the nightmare sky turns to\n"
    "blue, the heaps of monster corpses start \n"
    "to evaporate along with the evil stench \n"
    "that filled the air. Jeeze, maybe you've\n"
    "done it. Have you really won?\n"
    "\n"
    "Something rumbles in the distance.\n"
    "A blue light begins to glow inside the\n"
    "ruined skull of the demon-spitter."
)

T5TEXT = (
    "What now? Looks totally different. Kind\n"
    "of like King Tut's condo. Well,\n"
    "whatever's here can't be any worse\n"
    "than usual. Can it?  Or maybe it's best\n"
    "to let sleeping gods lie.."
)

T6TEXT = (
    "Time for a vacation. You've burst the\n"
    "bowels of hell and by golly you're ready\n"
    "for a break. You mutter to yourself,\n"
    "Maybe someone else can kick Hell's ass\n"
    "next time around. Ahead lies a quiet town,\n"
    "with peaceful flowing water, quaint\n"
    "buildings, and presumably no Hellspawn.\n"
    "\n"
    "As you step off the transport, you hear\n"
    "the stomp of a cyberdemon's iron shoe."
)

# Character cast strings
CC_ZOMBIE = "ZOMBIEMAN"
CC_SHOTGUN = "SHOTGUN GUY"
CC_HEAVY = "HEAVY WEAPON DUDE"
CC_IMP = "IMP"
CC_DEMON = "DEMON"
CC_LOST = "LOST SOUL"
CC_CACO = "CACODEMON"
CC_HELL = "HELL KNIGHT"
CC_BARON = "BARON OF HELL"
CC_ARACH = "ARACHNOTRON"
CC_PAIN = "PAIN ELEMENTAL"
CC_REVEN = "REVENANT"
CC_MANCU = "MANCUBUS"
CC_ARCH = "ARCH-VILE"
CC_SPIDER = "THE SPIDER MASTERMIND"
CC_CYBER = "THE CYBERDEMON"
CC_HERO = "OUR HERO"

# Misc. other strings.
SAVE_GAME_NAME = "doomsav"

# File locations,
# relative to current position.
# Path names are OS-sensitive.
DEVMAPS = "devmaps"
DEVDATA = "devdata"

endmsg = [
    QUIT_MSG,
    "please don't leave, there's more\ndemons to toast!",
    "let's beat it -- this is turning\ninto a bloodbath!",
    "i wouldn't leave if i were you.\ndos is much worse.",
    "you're trying to say you like dos\nbetter than me, right?",
    "don't leave yet -- there's a\ndemon around that corner!",
    "ya know, next time you come in here\ni'm gonna toast ya.",
    "go ahead and leave. see if i care."
    # QuitDOOM II messages
    "you want to quit?\nthen, thou hast lost an eighth!",
    "don't go now, there's a \ndimensional shambler waiting\nat the dos " "prompt!",
    "get outta here and go back\nto your boring programs.",
    "if i were your boss, i'd \n deathmatch ya in a minute!",
    "look, bud. you leave now\nand you forfeit your body count!",
    "just leave. when you come\nback, i'll be waiting with a bat.",
    "you're lucky i don't smack\nyou for thinking about leaving."
    # really?
    # "fuck you, pussy!\nget the fuck out!",
    # "you quit and i'll jizz\nin your cystholes!",
    # "if you leave, i'll make\nthe lord drink my jizz.",
    # "hey, ron! can we say\n'fuck' in the game?",
    # "i'd leave: this is just\nmore monsters and levels.\nwhat a load.",
    # "suck it down, asshole!\nyou're a fucking wimp!",
    # "don't quit now! we're \nstill spending your money!",
    # Internal debug. Different style, too.
    # "THIS IS NO MESSAGE!\nPage intentionally left blank.",
]

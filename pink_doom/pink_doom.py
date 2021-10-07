"""Main module."""
import sys

from pink_doom.doom.main import main
from pink_doom.misc import argv

if __name__ == "__main__":
    argv.my_argc = len(sys.argv) - 1
    argv.my_argv = sys.argv
    main()

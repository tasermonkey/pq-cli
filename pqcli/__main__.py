import argparse
from pathlib import Path

import xdg

from pqcli.roster import Roster
from pqcli.ui.basic import BasicUserInterface
from pqcli.ui.curses import CursesUserInterface
from pqcli.ui.urwid import UrwidUserInterface

SAVE_PATH = Path(xdg.XDG_CONFIG_HOME) / "pqcli" / "save.dat"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="pqcli")

    group = parser.add_mutually_exclusive_group()
    group.set_defaults(ui=UrwidUserInterface)
    group.add_argument(
        "--basic",
        dest="ui",
        action="store_const",
        const=BasicUserInterface,
        help="Use basic user interface (very crude, but uses least CPU)",
    )
    group.add_argument(
        "--curses",
        dest="ui",
        action="store_const",
        const=CursesUserInterface,
        help="Use curses user interface (fast, but no colors output)",
    )
    group.add_argument(
        "--urwid",
        dest="ui",
        action="store_const",
        const=UrwidUserInterface,
        help="Use curses user interface (slow, but rich colors output)",
    )

    parser.add_argument(
        "--no-colors",
        dest="colors",
        action="store_false",
        help="Disable color highlighting in curses and urwid interface",
    )

    parser.add_argument(
        "--no-save",
        dest="use_saves",
        action="store_false",
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--cheats", action="store_true", help="???")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    roster = Roster.load(SAVE_PATH)

    try:
        ui = args.ui(roster, args)
        ui.run()
    finally:
        if args.use_saves:
            roster.save()


if __name__ == "__main__":
    main()

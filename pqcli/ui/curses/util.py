import curses
import curses.ascii
import typing as T
from dataclasses import dataclass

KEYS_CYCLE = {curses.ascii.TAB}
KEYS_GV_CYCLE = KEYS_CYCLE | set(map(ord, ","))
KEYS_DOWN = set(map(ord, "jJ")) | {curses.KEY_DOWN}
KEYS_LEFT = set(map(ord, "hH")) | {curses.KEY_LEFT}
KEYS_RIGHT = set(map(ord, "lL")) | {curses.KEY_RIGHT}
KEYS_UP = set(map(ord, "kK")) | {curses.KEY_UP}
KEYS_CANCEL = set(map(ord, "qQ")) | {curses.ascii.ESC}
KEYS_PPAGE = set(map(ord, "nN")) | {curses.KEY_PPAGE}
KEYS_NPAGE = set(map(ord, "mM")) | {curses.KEY_NPAGE}

@dataclass
class Choice:
    keys: T.List[int]
    desc: str
    callback: T.Callable[..., T.Any]


def first(source: T.Iterable[T.Any], default: T.Any = None) -> T.Any:
    return next(iter(source), default)

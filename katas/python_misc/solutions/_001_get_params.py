# import curses
# from collections import namedtuple


# class Params(NamedTuple):
#     duration: int
#     interval: float

# # 1.1
# def create_params(...) -> Params:
#     return ...

# def get_params(stdscr):
#     params_dict: dict[str, int | float] = {}
#     # 2.1 clear screen
#     # 2.2 make sure user can see what they type

#     msg = "Enter timer duration in seconds: "
#     # 2.3 curset equivalent of print
#     # 2.4 curset equivalent of input()
#     duration_input = stdscr.getstr(0, len(msg) + 1)
#     # 2.5 wrap in error
#     try:
#         duration = int(duration_input)
#         if not 0 <= duration <= 10:
#             raise ValueError()
#         params_dict["duration"] = duration
#     except ValueError:
#         # 2.6 turn off curses and exits
#         curses.endwin()
#         print(
#             "Invalid input for duration. Please enter a valid integer between 0 and 10."
#         )
#         exit()
#     msg = "BPM: "
#     # 2.7 curset equivalent of print
#     params_dict["interval"] = 60 / int(...)

#     # 2.8 clear screen
#     # 2.9 stop displaying what the user typed

#     return create_params(...)  # 2.8 returns the actual named tuple


# def main(stdscr):
#     2.1 hide cursor
#     params = get_params(stdscr)
#     # 2.2 stop curses so that you can print
#     print(params)


# if __name__ == "__main__":
#     #     # 2.3 wraps in curses
#     print("DONE")


import curses
from typing import NamedTuple


class Params(NamedTuple):
    duration: int
    interval: float


def create_params(params_dict: dict) -> Params:
    return Params(**params_dict)


def get_params(stdscr: curses.window) -> NamedTuple:
    params_dict: dict[str, int | float] = {}
    stdscr.clear()
    curses.echo()

    msg = "Enter timer duration in seconds: "
    stdscr.addstr(msg)
    duration_input = stdscr.getstr(0, len(msg) + 1)
    try:
        duration = int(duration_input)
        if not 0 <= duration <= 10:
            raise ValueError()
        params_dict["duration"] = duration
    except ValueError:
        curses.endwin()
        print(
            "Invalid input for duration. Please enter a valid integer between 0 and 10."
        )
        exit()

    msg = "BPM: "
    stdscr.addstr(msg)
    params_dict["interval"] = 60 / int(stdscr.getstr(1, len(msg) + 1))

    stdscr.clear()
    curses.echo(False)

    return create_params(params_dict)


def main(stdscr):
    curses.curs_set(0)
    params = get_params(stdscr)
    curses.endwin()
    print(params)


if __name__ == "__main__":
    curses.wrapper(main)
    print("DONE")

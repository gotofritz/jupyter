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
#     # 2.5 wrap in error
#     try:
#         duration = int(user_input)
#         ...
#             raise ...
#         params_dict["duration"] = duration
#     except ValueError:
#         # 2.6 turn off curses and exits
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
#     2.11 hide cursor
#     params = get_params(stdscr)
#     # 2.2 stop curses so that you can print
#     print(params)


# if __name__ == "__main__":
#     #     # 2.3 wraps in curses
#     print("DONE")

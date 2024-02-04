# import curses
# import threading
# import time
# from ._001_get_params import get_params


# def timer(stop_event, timer_duration):
#     time.sleep(timer_duration)
#     3.6 sets the stop_event


# def main(stdscr):
#     stop_event = None
#     try:
#         # 3.1 Hide cursor

#         params = get_params(stdscr)

#         stdscr.clear()
#         stdscr.refresh()

#         stop_event = ... 3.2

#         # cap the whole program length
#         main_thread = ... 3.3
#         3.4

#         3.5 # Wait for all events to stop
#
#         curses.endwin()
#         print(f"\nRun for {params.duration} secs")
#     except ... 2.1:
#         # 2.2 exit curses
#         print("\nProgram terminated by user.")

#     finally:
#         if stop_event:
#             3.7 # Signal the printing thread to stop
#


# if __name__ == "__main__":
#     curses.wrapper(main)
#     print("DONE")

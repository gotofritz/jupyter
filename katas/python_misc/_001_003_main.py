# import curses
# import threading
# import time
# from ._001_get_params import get_params


# def print_beat(win: curses.window, stop_event, interval):
#     win.clear()
#     time_signature = 4
#     BEAT = ".  "
#     count = 0
#     while not stop_event.is_set():
#         if count == time_signature:
#             win.clear()
#             count = 0
#         win.addstr(0, count * len(BEAT), BEAT)
#         win.refresh()
#         count += 1
#         time.sleep(interval)


# def timer(stop_event, timer_duration):
#     time.sleep(timer_duration)
#     stop_event.set()


# def main(stdscr):
#     stop_event = None
#     try:
#         curses.curs_set(0)

#         params = get_params(stdscr)

#         stdscr.clear()
#         stdscr.refresh()

#         stop_event = threading.Event()

#         metronome_win = ... 2.1

#         metronome_thread = ... 2.2
#         metronome_thread.start()

#         # cap the whole program length
#         main_thread = threading.Thread(target=timer, args=(stop_event, params.duration))
#         main_thread.start()

#         # Wait for all events to stop
#         main_thread.join()
#         curses.endwin()
#         print(f"\nRun for {params.duration} secs")
#     except KeyboardInterrupt:
#         curses.endwin()
#         print("\nProgram terminated by user.")

#     finally:
#         if stop_event:
#             # Signal the printing thread to stop
#             stop_event.set()
#             ... 2.3 make sure script is not hanging waiting for thread to finish


# if __name__ == "__main__":
#     curses.wrapper(main)
#     print("DONE")

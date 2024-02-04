# import curses
# from textwrap import dedent
# import threading
# import time
# from ._001_get_params import get_params
# from ._001_shuffling_iterator import ShufflingIterator
# from ._001_constants import notes, intervals, directions


# class NotesGenerator:
#     def __init__(self):
#         self.notes = ShufflingIterator(notes)
#         self.intervals = ShufflingIterator(intervals)
#         self.directions = ShufflingIterator(directions)

#     def generate(self):
#         return dedent(
#             f"""
#                   NOTE: {next(self.notes)}
#               INTERVAL: {next(self.intervals)}
#              DIRECTION: {next(self.directions)}
#             """
#         ).strip("\n")


# def listen_for_key(win: curses.window, notes_generator, stop_event, interval):
#     ... 2.1 make it non-blocking
#     win.clear()
#     win.addstr(0, 0, notes_generator.generate())
#     win.refresh()
#     while not stop_event.is_set():
#         time.sleep(interval)
#         key = .. 2.3
#         if key != -1:
#             win.clear()
#             win.addstr(0, 0, notes_generator.generate())
#             win.refresh()


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
#         curses.curs_set(0)  # Hide cursor

#         params = get_params(stdscr)

#         stdscr.clear()
#         stdscr.refresh()

#         stop_event = threading.Event()

#         metronome_win = curses.newwin(1, 15, 0, 0)
#         metronome_thread = threading.Thread(
#             target=print_beat,
#             args=(metronome_win, stop_event, params.interval),
#         )
#         metronome_thread.start()

#         message_win = ... 3.1
#         key_thread = threading.Thread(
#             target=listen_for_key,
#             args=(message_win, NotesGenerator(), stop_event, params.interval),
#         )
#         key_thread.start()

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
#             metronome_thread.join()
#             key_thread.join()


# if __name__ == "__main__":
#     curses.wrapper(main)
#     print("DONE")

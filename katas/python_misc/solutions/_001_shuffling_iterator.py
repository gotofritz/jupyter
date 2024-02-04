# import random
# import string
# import threading


# class ShufflingIterator:
#     def __init__(self, items, debug=False):
#         self.debug = debug
#         self.index = 0
#         self.lock = ... 2.1
#         if self.debug:
#             self.items = ["--"] + items
#         else:
#             self.items = items
#         self._reset()

#     def __iter__(self):
#         ... 2.3

#     def __next__(self):
#         ... 2.4
#             self._reset()
#             current_number = self.items[self.index]
#             self.index += 1
#             return current_number

#     def _reset(self):
#         if self.index >= len(self.items):
#             if self.debug:
#                 ... 2.5
#             else:
#                 random.shuffle(self.items)
#             self.index = 0


# if __name__ == "__main__":
#     five_letters = ...3.1
#     name = ShufflingIterator(five_letters, True)
#     for _ in range(24):
#         print(next(name))
#     print("DONE")


import random
import string
import threading


class ShufflingIterator:
    def __init__(self, items, debug=False):
        self.debug = debug
        self.index = 0
        self.lock = threading.Lock()
        if self.debug:
            self.items = ["--"] + items
        else:
            self.items = items
        self._reset()

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            self._reset()
            current_number = self.items[self.index]
            self.index += 1
            return current_number

    def _reset(self):
        if self.index >= len(self.items):
            if self.debug:
                self.items[1:] = random.sample(self.items[1:], k=len(self.items) - 1)
            else:
                random.shuffle(self.items)
            self.index = 0


if __name__ == "__main__":
    five_letters = list(string.ascii_uppercase)[:5]
    name = ShufflingIterator(five_letters, True)
    for _ in range(24):
        print(next(name))
    print("DONE")

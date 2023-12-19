import time


1


def cpu_bound(number):
    return sum(i * i for i in range(number))


2


def find_sums(numbers):
    ...


3
if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.perf_counter()
    find_sums(numbers)
    duration = time.perf_counter() - start_time
    print(f"Duration {duration} seconds")

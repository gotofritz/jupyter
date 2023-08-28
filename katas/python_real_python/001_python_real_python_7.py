import multiprocessing
import time


1


def cpu_bound(number):
    return sum(i * i for i in range(number))


2


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


3
if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

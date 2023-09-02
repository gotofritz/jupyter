import requests
import multiprocessing
import time

sites = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 80


1


def set_global_session():
    ...


2


def download_site(url):
    ...
    print(f"{name}:Read {len(response.content)} from {url}")


3


def download_all_sites(sites):
    ...


4
if __name__ == "__main__":
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"\nDownloaded {len(sites)} in {duration} seconds")

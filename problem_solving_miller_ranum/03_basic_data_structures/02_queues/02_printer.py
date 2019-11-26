import sys

sys.path.append("..")  # allow import of code from one directory level up

from data_structures import Queue
from typing import List
import random

random.seed(190818)


class Printer(object):
    def __init__(self, pages_per_minute: float) -> None:
        self.page_rate = pages_per_minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self) -> None:
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self) -> bool:
        return self.current_task != None

    def start_next(self, new_task: "Task") -> None:
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60.0 / self.page_rate


class Task(object):
    def __init__(self, start_time: int) -> None:
        self.start_time = start_time
        self.pages = random.randrange(1, 21)

    def get_start_time(self) -> int:
        return self.start_time

    def get_pages(self) -> int:
        return self.pages

    def wait_time(self, current_time: int) -> int:
        return current_time - self.start_time


def new_print_task() -> bool:
    return random.randrange(1, 181) == 180


def simulation(num_seconds: int, pages_per_minute: int) -> None:

    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        # mutually exclusive with the condition above because if we
        # have just added a task, print_queue will not be empty
        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        # tick every second
        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)

    print(
        "Average Wait: %6.2f secs, %1d tasks remaining."
        % (average_wait, print_queue.size())
    )


if __name__ == "__main__":
    for _ in range(10):
        simulation(3600, 5)

import random
import time
from threading import Thread
from queue import Queue
from random import randint


class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        minimal = min(len(list(guests)), len(self.tables))
        for i in range(minimal):
            self.tables[i].guest = guests[i]
            thread_1 = guests[i]
            thread_1.start()
            print(f'{list(guests)[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len(list(guests)) > minimal:
            for i in range(minimal, len(list(guests))):
                self.queue.put(guests[i])
                print(f'{list(guests)[i].name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread_1 = table.guest
                    thread_1.start()


guests_names = ["Мария", "Людмила", "Олег", "Юлия", "Ольга", "Артем", "Андрей", "Ева", "Игнат", "Анна", "Илья", "Джон"]

tables = [Table(number) for number in range(1, 6)]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
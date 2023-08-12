import time
from abc import ABC, abstractmethod

from datetime import datetime
from Encoder import Encoder
from twenty48.Game import Game
from twenty48.Input import Input
from twenty48.Display import NoneDisplay


class Reporter(ABC):

    @abstractmethod
    def __init__(self, input_:Input):
        pass

    @abstractmethod
    def generate_report(self, num_games: int):
        pass


class FileReporter(Reporter):
    # Plays n games and saves gameinfo objects as a binary file for efficient storage

    def __init__(self, input_:Input, encoder: Encoder, filename: str = None):
        self.input = input_
        self.display = NoneDisplay()
        self.encoder = encoder
        if filename is None:
            self.filename = str(datetime.now()) + ".txt"
        else:
            self.filename = filename

    def generate_report(self, num_games: int = 5):
        t = time.perf_counter()
        print(f"Saving to {self.filename}")
        for i in range(num_games):
            g = Game(display=self.display, input=self.input)
            info = g.play_game()
            self.encoder.encode(gameinfo=info, filename=self.filename)
            print(f"Game number {i+1} completed", end='\r')
        t = time.perf_counter() - t
        print(f"All games completed in {t} seconds")





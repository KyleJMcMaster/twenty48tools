import pickle
from abc import ABC
from twenty48.GameInformation import GameInformation
from typing import List


class Decoder(ABC):
    @staticmethod
    def decode(filename: str) -> GameInformation:
        pass


class PickleDecoder(Decoder):

    @staticmethod
    def decode(filename: str) -> List[GameInformation]:
        info = []
        with open(filename, 'rb') as file:
            while True:
                try:
                    info.append(pickle.load(file))
                except EOFError:
                    break
        return info


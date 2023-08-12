from twenty48game.GameInformation import GameInformation
from typing import List


class Statistics:

    @staticmethod
    def avg_score(games: List[GameInformation]):
        scores = []
        for game in games:
            scores.append(game.score)
        return float(sum(scores))/float(len(scores))



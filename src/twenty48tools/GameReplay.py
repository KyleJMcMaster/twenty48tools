from twenty48.GameInformation import GameInformation
from twenty48.Display import Display


class GameReplay:

    def __init__(self, display:Display):
        self.display = display

    def replay(self, game: GameInformation):
        turns = game.turns

        for turn in game.turns:
            self.display.display_board(turn.board.get_board_from_text_rep())
            input()

import Move
import random

class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "0"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if self._is_human:
            self._marker = Player.PLAYER_MARKER

        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter a valid no between (1-9)")
        return move

    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print("Computer Move:", move.value)
        return move


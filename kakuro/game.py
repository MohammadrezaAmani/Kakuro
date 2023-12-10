from kakuro.board import Board
from kakuro.node import Node


class Game:
    """
    Represents a Kakuro game.

    Args:
        board (Board): The game board.

    Attributes:
        board (Board): The game board.

    Methods:
        optimize: Optimizes the game.
        run: Runs the game.
        test: Runs a test on the game.

    """

    def __init__(self, board: Board) -> None:
        self.board = Board(board)

    def optimize(self, depth: int = 3) -> None:
        """
        Optimize the game by applying a depth-limited search algorithm.

        Parameters:
        - depth (int): The maximum depth of the search algorithm. Defaults to 3.
        """
        ...

    def run(self) -> None:
        """
        Run the game.
        """
        ...

    def test(self) -> None:
        """
        This method is used to test the functionality of the game.

        It creates four nodes, performs some operations on them, and prints the results.
        """
        n1 = Node(0, 0, "#", 0, 16, 2)
        n2 = Node(1, 0, 17, 2, "#", 0)
        n3 = Node(0, 1, "#", 0, 10, 2)
        n4 = Node(1, 1, 9, 2, "#", 0)

        print("-----------------------------------")
        for i in [n1, n3]:
            print("down", i, i.combinations_down)
            print("value_down", i, i.value_down)
        for i in [n2, n4]:
            print("right", i, i.combinations_right)
            print("value_right", i, i.value_right)
        self.board.remove_non_intersection(0, 0, n2, n1)
        for i in range(0, 5):
            n2, n1 = self.board.remove_non_intersection(0, 0, n2, n1)
            n2, n3 = self.board.remove_non_intersection(0, 1, n2, n3)
            n4, n1 = self.board.remove_non_intersection(1, 0, n4, n1)
            n4, n3 = self.board.remove_non_intersection(1, 1, n4, n3)

        print("-----------------------------------")
        for i in [n1, n3]:
            print("down", i, i.combinations_down)
            print("value_down", i, i.value_down)
        for i in [n2, n4]:
            print("right", i, i.combinations_right)
            print("value_right", i, i.value_right)

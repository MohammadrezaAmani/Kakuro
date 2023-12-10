from kakuro.node import Node
from kakuro.config import Config


class Board:
    """
    Represents a Kakuro board.

    Attributes:
        board (list): The board representation as a 2D list of Node objects.
    """

    def __init__(self, board) -> None:
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        if isinstance(value, Board):
            self.board = value.board
        self._board = value
        self._board = self.create_board(self._board)

    def create_board(self, text: str):
        """
        Create the board from the given text representation.

        Args:
            text (str): The text representation of the board.

        Returns:
            list: The board representation as a 2D list of Node objects.
        """
        board = []
        for i in text.strip().split("\n"):
            board2 = []
            count = 0
            for j in i.strip().split():
                count += 1
                if j.strip() == Config.EMPTY:
                    node = Node(len(board), count, Config.EMPTY, 0, Config.EMPTY, 0)
                elif Config.SEP in j:
                    j1 = j.split(Config.SEP)[0]
                    j2 = j.split(Config.SEP)[1]
                    if j1 != Config.EMPTY:
                        j1 = int(j1)
                    if j2 != Config.EMPTY:
                        j2 = int(j2)
                    node = Node(len(board), count, j2, 0, j1, 0)
                elif j.strip() == Config.UNKNOWN:
                    node = Node(len(board), count, Config.UNKNOWN, 0, Config.UNKNOWN, 0)
                board2.append(node)
            board.append(board2)
        return board

    def __str__(self) -> str:
        text = ""
        for i in self.board:
            for j in i:
                text += str(j) + "\t"
            text += "\n"
        return text

    def remove_non_intersection(
        self, x: int, y: int, node1: Node, node2: Node
    ) -> (Node, Node):
        """
        Remove non-intersecting combinations from the given nodes.

        Args:
            x (int): The x-coordinate of the intersection.
            y (int): The y-coordinate of the intersection.
            node1 (Node): The first node.
            node2 (Node): The second node.

        Returns:
            tuple: The updated node1 and node2 with non-intersecting combinations removed.
        """
        uniqe = []
        uniqe2 = []
        for i in node1.combinations_right:
            for j in i:
                if j not in uniqe:
                    uniqe.append(j)
        for i in node2.combinations_down:
            for j in i:
                if j not in uniqe2:
                    uniqe2.append(j)

        intersection = []
        for i in uniqe:
            if i in uniqe2 and i:
                intersection.append(i)
        resy1 = []
        for i in intersection:
            for j in node1.combinations_right:
                if i in j and j.index(i) == x:
                    resy1.append(j)
        resy2 = []
        for i in intersection:
            for j in node2.combinations_down:
                if i in j and j.index(i) == y:
                    resy2.append(j)

        node1.combinations_right = resy1
        node2.combinations_down = resy2
        return node1, node2

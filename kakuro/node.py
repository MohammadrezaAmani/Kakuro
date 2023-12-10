class Node:
    def __init__(
        self,
        x: int,
        y: int,
        right: int | str,
        space_right: int,
        down: int | str,
        space_down: int,
    ) -> None:
        """
        Initialize a Node object.

        Args:
            x (int): The x-coordinate of the node.
            y (int): The y-coordinate of the node.
            right (int | str): The sum or clue for the right direction. If it's a clue, it should be a string.
            space_right (int): The number of empty spaces to the right of the node.
            down (int | str): The sum or clue for the down direction. If it's a clue, it should be a string.
            space_down (int): The number of empty spaces below the node.
        """
        self.x = x
        self.y = y
        self.right = right
        self.down = down
        self.space_right = space_right if isinstance(self.right, int) else 0
        self.space_down = space_down
        self.combinations_right = (
            self.find(self.right, self.space_right)
            if isinstance(self.right, int)
            else []
        )
        self.combinations_down = (
            self.find(self.down, self.space_down) if isinstance(self.down, int) else []
        )
        self.value_right = (
            [0 for i in range(self.space_right)] if isinstance(self.right, int) else []
        )
        self.value_down = (
            [0 for i in range(self.space_down)] if isinstance(self.down, int) else []
        )

    @property
    def space_down(self):
        return self._space_down

    @space_down.setter
    def space_down(self, value):
        """
        Setter for the space_down property.

        Args:
            value: The value to set for the space_down property.
        """
        if isinstance(self.down, str):
            self._space_down = 0
            return
        self._space_down = value
        self.value_down = (
            [0 for i in range(self.space_down)] if isinstance(self.down, int) else []
        )
        self.combinations_down = (
            self.find(self.down, self.space_down) if isinstance(self.down, int) else []
        )
        self.check_value("down")

    @property
    def space_right(self):
        return self._space_right

    @space_right.setter
    def space_right(self, value):
        """
        Setter for the space_right property.

        Args:
            value: The value to set for the space_right property.
        """
        if isinstance(self.right, str):
            self._space_right = 0
            return
        self._space_right = value
        self.value_right = (
            [0 for i in range(self.space_right)] if isinstance(self.right, int) else []
        )
        self.combinations_right = (
            self.find(self.right, self.space_right)
            if isinstance(self.right, int)
            else []
        )

    @property
    def combinations_right(self):
        return self._combinations_right

    @combinations_right.setter
    def combinations_right(self, value):
        """
        Setter for the combinations_right property.

        Args:
            value: The value to set for the combinations_right property.
        """
        self._combinations_right = value.copy()
        self.check_value("right")

    @property
    def combinations_down(self):
        return self._combinations_down

    @combinations_down.setter
    def combinations_down(self, value):
        """
        Setter for the combinations_down property.

        Args:
            value: The value to set for the combinations_down property.
        """
        self._combinations_down = value.copy()
        self.check_value("down")

    def check_value(self, direction: str = "right"):
        """
        Check the value of the node in the specified direction and update the corresponding value list.

        Args:
            direction (str): The direction to check the value. Can be "right" or "down".
        """
        if direction == "right":
            for i in range(len(self.combinations_right)):
                for j in range(len(self.combinations_right[i])):
                    flag = True
                    for k in range(len(self.combinations_right)):
                        if (
                            self.combinations_right[i][j]
                            != self.combinations_right[k][j]
                        ):
                            flag = False
                            break
                    if flag:
                        self.value_right[j] = self.combinations_right[i][j]
        elif direction == "down":
            for i in range(len(self.combinations_down)):
                for j in range(len(self.combinations_down[i])):
                    flag = True
                    for k in range(len(self.combinations_down)):
                        if self.combinations_down[i][j] != self.combinations_down[k][j]:
                            flag = False
                            break
                    if flag:
                        self.value_down[j] = self.combinations_down[i][j]

    def __repr__(self):
        return f"({self.down}\{self.right})"

    def __str__(self) -> str:
        return self.__repr__()

    def find_combinations(self, value: int, space: int, combination: list):
        """
        Find all possible combinations of numbers that sum up to the given value with the given number of spaces.

        Args:
            value (int): The target sum value.
            space (int): The number of spaces available.
            combination (list): The current combination of numbers.

        Returns:
            None
        """
        if space == 0 and value == 0:
            self._combinations.append(combination)
            return
        if 0 == space or value < 0:
            return
        for i in range(1, 10):
            if i not in combination:
                self.find_combinations(value - i, space - 1, combination + [i])

    def find(self, value, space):
        """
        Find all possible combinations of numbers that sum up to the given value with the given number of spaces.

        Args:
            value: The target sum value.
            space: The number of spaces available.

        Returns:
            list: A list of all possible combinations of numbers.
        """
        self._combinations = []
        self.find_combinations(value, space, [])
        return self._combinations.copy()

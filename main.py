from kakuro import Game

board = """
#     #     #     24|#  16|#
#     #     6|17  ?     ?
#     17|18 ?     ?     ?
#|17  ?     ?     ?     #
#|11  ?     ?     #     #
"""

if __name__ == "__main__":
    game = Game(board)
    game.run(depth=3)
    print(game)

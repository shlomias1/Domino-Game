import random
from Linked_List import LinkedList

class DominoGame:
    def __init__(self, num_players):
        if not (2 <= num_players <= 4):
            raise ValueError("Number of players must be between 2 and 4")
        self.num_players = num_players
        self.players = [[] for _ in range(num_players)]
        self.board = LinkedList()
        self.stock = self.generate_domino_set()
        self.current_player = 0
        self.distribute_tiles()

    def generate_domino_set(self):
        tiles = [(i, j) for i in range(7) for j in range(i, 7)]
        random.shuffle(tiles)
        return tiles

    def distribute_tiles(self):
        num_tiles = 7 if self.num_players == 2 else 5
        for i in range(self.num_players):
            for _ in range(num_tiles):
                self.players[i].append(self.stock.pop())

    def valid_moves(self, tile):
        if not self.board.head:
            return True
        left = self.board.head.value[0]
        right = self.board.tail.value[1]
        return tile[0] == left or tile[1] == left or tile[0] == right or tile[1] == right

    def play_tile(self, player_idx, tile):
        left = self.board.head.value[0] if self.board.head else None
        right = self.board.tail.value[1] if self.board.tail else None

        if not self.board.head:
            self.board.add_to_head(tile)
        elif tile[1] == left:
            self.board.add_to_head((tile[1], tile[0]))
        elif tile[0] == left:
            self.board.add_to_head(tile)
        elif tile[0] == right:
            self.board.add_to_tail(tile)
        elif tile[1] == right:
            self.board.add_to_tail((tile[1], tile[0]))
        else:
            return False  # invalid move

        self.players[player_idx].remove(tile)
        return True

    def draw_tile(self, player_idx):
        if self.stock:
            tile = self.stock.pop()
            self.players[player_idx].append(tile)
            return tile
        return None

    def current_board(self):
        return self.board.to_list()

    def has_winner(self):
        for i, hand in enumerate(self.players):
            if not hand:
                return i
        return None

    def next_turn(self):
        self.current_player = (self.current_player + 1) % self.num_players

    def player_hand(self, player_idx):
        return self.players[player_idx]
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.self_pieces()


    def self_pieces(self): #This method’s job is to put the right "letter" in the right "index" of your self.grid.
        black_back_rank = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        white_back_rank = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

        self.grid[0] = black_back_rank
        self.grid[7] = white_back_rank

        self.grid[1] = ['p'] * 8
        self.grid[6] = ['P'] * 8

    def display(self):
        for _ in self.grid:
            print(_)

    def move_piece(self, start_pos, end_pos):
        # Step 1: Unpack the coordinates
        r1, c1 = start_pos #(row, col) tuples
        r2, c2 = end_pos #(row, col) tuples

        # Step 2 & 3: Take the piece from start and put it at end
        piece = self.grid[r1][c1]
        self.grid[r2][c2] = piece

        # Step 4: Make the starting square empty
        self.grid[r1][c1] = None





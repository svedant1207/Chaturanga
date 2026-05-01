class Board:
    def __init__(self):
        # Create an 8x8 grid filled with None (empty squares)
        # grid[0] is the top row (black's back rank, rank 8)
        # grid[7] is the bottom row (white's back rank, rank 1)
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Each piece is represented as a 2-character string:
        # First character = color ('w' for white, 'b' for black)
        # Second character = piece type (R=Rook, N=Knight, B=Bishop, Q=Queen, K=King, P=Pawn)
        # Example: 'wR' = white Rook, 'bK' = black King

        black_back_rank = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
        white_back_rank = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']

        # Use [:] to copy the list — avoids both rows pointing to the same list object
        self.grid[0] = black_back_rank[:]  # rank 8 — black's back rank
        self.grid[7] = white_back_rank[:]  # rank 1 — white's back rank

        # Fill pawn rows
        self.grid[1] = ['bP' for _ in range(8)]  # rank 7 — black pawns
        self.grid[6] = ['wP' for _ in range(8)]  # rank 2 — white pawns

        # Rows 2-5 (ranks 3-6) stay None — empty squares in the middle

    def in_bounds(self, row, col):
        # Returns True if (row, col) is a valid square on the board
        # Used by move generators to avoid IndexError when going off the edge
        return 0 <= row <= 7 and 0 <= col <= 7

    def get_piece(self, row, col):
        # Returns the piece string at (row, col), or None if the square is empty
        # Keeps grid access in one place — easier to change later if needed
        return self.grid[row][col]

    def display(self):
        # Prints each row of the grid on its own line
        # Useful for debugging in the terminal while building the engine
        for row in self.grid:
            print(row)

    def move_piece(self, start_pos, end_pos):
        # Moves a piece from start_pos to end_pos on the raw grid
        # Does NOT check legality — that is GameState's responsibility
        # Returns the captured piece (or None) so GameState can store it for undo_move

        r1, c1 = start_pos  # unpack starting square
        r2, c2 = end_pos    # unpack destination square

        piece = self.grid[r1][c1]       # grab the piece being moved
        captured = self.grid[r2][c2]    # store whatever is on the destination (may be None)

        self.grid[r2][c2] = piece       # place the piece on the destination
        self.grid[r1][c1] = None        # vacate the starting square

        return captured                 # GameState stores this so undo_move can restore it
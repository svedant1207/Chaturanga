from chess_engine.board import Board

def test_black_back_rank_is_correct():
    # Check that black's back rank is set up in the right order at row 0
    board = Board()
    assert board.grid[0] == ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']


def test_white_back_rank_is_correct():
    # Check that white's back rank is set up in the right order at row 7
    board = Board()
    assert board.grid[7] == ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']


def test_black_pawns_on_row_1():
    # Black pawns should fill all 8 squares of row 1
    board = Board()
    assert board.grid[1] == ['bP'] * 8


def test_white_pawns_on_row_6():
    # White pawns should fill all 8 squares of row 6
    board = Board()
    assert board.grid[6] == ['wP'] * 8


def test_middle_of_board_is_empty():
    # Rows 2 to 5 are the empty middle of the board at the start
    # Every single square in those rows should be None
    board = Board()
    for row in range(2, 6):
        for col in range(8):
            assert board.grid[row][col] is None


def test_in_bounds_valid_squares():
    # Corners of the board are the extreme valid squares
    # Both should return True
    board = Board()
    assert board.in_bounds(0, 0) is True   # top left corner
    assert board.in_bounds(7, 7) is True   # bottom right corner


def test_in_bounds_invalid_squares():
    # Anything outside 0-7 range is off the board
    # Both should return False
    board = Board()
    assert board.in_bounds(-1, 0) is False  # one row above the board
    assert board.in_bounds(8, 0) is False   # one row below the board


def test_move_piece_moves_correctly():
    # Move a white pawn from its starting square (6,0) forward to (4,0)
    # The piece should appear at the destination and the source should be empty
    board = Board()
    board.move_piece((6, 0), (4, 0))
    assert board.get_piece(4, 0) == 'wP'  # piece arrived at destination
    assert board.get_piece(6, 0) is None  # starting square is now empty


def test_move_piece_returns_captured_piece():
    # Manually place a black pawn at (4,0) so white can capture it
    # move_piece should return the captured piece, not None
    board = Board()
    board.grid[4][0] = 'bP'
    captured = board.move_piece((6, 0), (4, 0))
    assert captured == 'bP'  # the black pawn was captured and returned
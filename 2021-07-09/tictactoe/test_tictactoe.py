import pytest

from tictactoe import TicTacToe


@pytest.fixture
def game():
    return TicTacToe()

def test_illegal_move(monkeypatch, game):
    board = [
        ["X", " ", "X"],
        [" ", "O", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)

    with pytest.raises(ValueError):
        game.play_at(0, 0)

    with pytest.raises(ValueError):
        game.play_at(0, 2)

    with pytest.raises(ValueError):
        game.play_at(1, 1)

    with pytest.raises(ValueError):
        game.play_at(2, 1)

    with pytest.raises(ValueError):
        game.play_at(3, 1)

    with pytest.raises(ValueError):
        game.play_at(0, 3)

    with pytest.raises(ValueError):
        game.play_at(5, 3)

    with pytest.raises(ValueError):
        game.play_at(-1, 1)

    with pytest.raises(ValueError):
        game.play_at(2, -1)

    with pytest.raises(ValueError):
        game.play_at(-2, -2)

def test_legal_move_X_1_2(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", "O", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)

    game.play_at(1,2)
    target_board = [
        ["X", " ", "X"],
        [" ", "O", "X"],
        [" ", "O", " "],
    ]
    assert game.board == target_board

def test_legal_move_X_0_1(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", "O", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)

    game.play_at(0,1)
    target_board = [
        ["X", "X", "X"],
        [" ", "O", " "],
        [" ", "O", " "],
    ]
    assert game.board == target_board

def test_legal_move_X_1_1(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", "O", "O"],
    ]
    monkeypatch.setattr(game, "board", board)

    game.play_at(1,1)
    target_board = [
        ["X", " ", "X"],
        [" ", "X", " "],
        [" ", "O", "O"],
    ]
    assert game.board == target_board

def test_legal_move_X_2_0(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", "O", "O"],
    ]
    monkeypatch.setattr(game, "board", board)

    game.play_at(2,0)
    target_board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        ["X", "O", "O"],
    ]
    assert game.board == target_board

def test_legal_move_O_1_2(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")

    game.play_at(1,2)
    target_board = [
        ["X", " ", "X"],
        [" ", " ", "O"],
        [" ", "O", " "],
    ]
    assert game.board == target_board

def test_legal_move_O_0_1(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")

    game.play_at(0,1)
    target_board = [
        ["X", "O", "X"],
        [" ", " ", " "],
        [" ", "O", " "],
    ]
    assert game.board == target_board

def test_legal_move_O_1_1(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")

    game.play_at(1,1)
    target_board = [
        ["X", " ", "X"],
        [" ", "O", " "],
        [" ", "O", " "],
    ]
    assert game.board == target_board

def test_legal_move_O_2_0(game, monkeypatch):
    board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")

    game.play_at(2,0)
    target_board = [
        ["X", " ", "X"],
        [" ", " ", " "],
        ["O", "O", " "],
    ]
    assert game.board == target_board

def test_moves_left(game):
    assert game.moves_left == 9

    game.play_at(1, 1)
    assert game.moves_left == 8

    game.play_at(0, 0)
    assert game.moves_left == 7

    game.play_at(2, 1)
    assert game.moves_left == 6

def test_next_player(game):
    assert game.current_player == "X"
    assert game.next_player() == "O"
    assert game.next_player() == "X"
    assert game.next_player() == "O"

def test_next_player_0_moves_left(game, monkeypatch):
    monkeypatch.setattr(game, "moves_left", 0)
    assert game.next_player() is None

def test_next_player_after_win(game, monkeypatch):
    monkeypatch.setattr(game, "get_winner", lambda: "X")
    assert game.next_player() is "X"

    monkeypatch.setattr(game, "current_player", "O")
    monkeypatch.setattr(game, "get_winner", lambda: "O")
    assert game.next_player() is "O"

def test_get_winner_not_over(game, monkeypatch):
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")
    assert game.get_winner() is False

    board = [
        [" ", " ", " "],
        [" ", "O", " "],
        [" ", " ", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() is False

    board = [
        ["X", "X", " "],
        ["O", "O", " "],
        [" ", " ", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() is False

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() is False

def test_get_winner_X(game, monkeypatch):
    board = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() == "X"

    board = [
        ["X", " ", " "],
        ["O", "X", " "],
        ["O", " ", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() == "X"

    board = [
        ["O", " ", "X"],
        ["O", "X", " "],
        ["X", " ", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() == "X"

    board = [
        ["X", " ", " "],
        ["X", "O", " "],
        ["X", "O", " "],
    ]
    monkeypatch.setattr(game, "board", board)
    assert game.get_winner() == "X"

def test_get_winner_O(game, monkeypatch):
    board = [
        ["X", "X", " "],
        ["O", "O", "O"],
        [" ", " ", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")
    assert game.get_winner() == "O"

    board = [
        ["X", " ", "O"],
        [" ", "O", "X"],
        ["O", " ", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")
    assert game.get_winner() == "O"

    board = [
        ["O", "X", " "],
        ["O", " ", "X"],
        ["O", " ", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "current_player", "O")
    assert game.get_winner() == "O"

def test_get_winner_tie(game, monkeypatch):
    board = [
        ["O", "X", "O"],
        ["X", "O", "X"],
        ["X", "O", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "moves_left", 0)
    assert game.get_winner() is None

    board = [
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "O", "X"],
    ]
    monkeypatch.setattr(game, "board", board)
    monkeypatch.setattr(game, "moves_left", 0)
    assert game.get_winner() is None
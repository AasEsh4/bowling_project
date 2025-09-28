from fixed_bowling_game import BowlingGame

def play_game(rolls):
    game = BowlingGame()
    for pins in rolls:
        game.roll(pins)
    return game

def test_gutter_game():
    game = play_game([0] * 20)
    assert game.score() == 0

def test_all_ones():
    """All rolls knock down 1 pin → score should be 20"""
    game = play_game([1] * 20)
    assert game.score() == 20
    
def test_single_spare():
    """5 + 5 (spare) followed by 3 → score should include bonus"""
    rolls = [5, 5, 3] + [0] * 17
    game = play_game(rolls)
    assert game.score() == 16  # (10 + 3) + 3
    
def test_single_strike():
    """10 (strike) followed by 3 + 4 → score should include bonus"""
    rolls = [10, 3, 4] + [0] * 16
    game = play_game(rolls)
    assert game.score() == 24  # 10 + (3 + 4) + 3 + 4
    
def test_perfect_game():
    """12 strikes → maximum score of 300"""
    game = play_game([10] * 12)
    assert game.score() == 300
    
def test_all_spares():
    """21 rolls of 5 → every frame is a spare → total = 150"""
    game = play_game([5] * 21)
    assert game.score() == 150
    
def test_regular_game_example():
    """
    Game with no strikes or spares:
    Rolls: [3, 4, 2, 5, 1, 6, 4, 2, 8, 1,
            7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
    Expected total = 72
    """
    rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1,
             7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
    game = play_game(rolls)
    assert game.score() == 72
    
def test_example_game():
    """Complex mixed game → expected score = 190"""
    rolls = [10, 3, 6, 5, 5, 8, 1,
             10, 10, 10, 9, 0, 7, 3,
             10, 10, 8]
    game = play_game(rolls)
    assert game.score() == 190

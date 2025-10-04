def calculate_elo(
    elo_a: float, elo_b: float, k: float, result: int
) -> tuple[float, float]:
    """
    Calculates the ELO change between two players with a given result.

    Args:
        elo_a(int): The ELO rating of player A.
        elo_b(int): The ELO rating of player B.
        result(int): The result of the match (1 for win for player A, 0 for loss for player A, 0.5 for draw).

    Returns:
        tuple[int, int]: The new ELO ratings for player A and player B.
    """
    expected_a: float = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))
    expected_b: float = 1 / (1 + 10 ** ((elo_a - elo_b) / 400))

    new_elo_a: float = elo_a + k * (result - expected_a)
    new_elo_b: float = elo_b + k * ((1 - result) - expected_b)

    return new_elo_a, new_elo_b

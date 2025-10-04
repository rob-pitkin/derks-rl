import unittest
from utils import calculate_elo


class TestEloRating(unittest.TestCase):
    def test_elo_rating(self):
        elo_a = 1200
        elo_b = 1000
        result = 1
        k = 30

        new_elo_a, new_elo_b = calculate_elo(elo_a, elo_b, result=result, k=k)

        self.assertAlmostEqual(new_elo_a, 1207.2, 1)
        self.assertAlmostEqual(new_elo_b, 992.8, 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()

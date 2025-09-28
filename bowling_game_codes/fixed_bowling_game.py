"""

Bowling Game Implementation (Refactored & Debugged Version)

This module provides a Python class for simulating and scoring 
a 10-pin bowling game, according to official bowling rules.

Features:
- Supports 10 frames per game
- Correctly handles strikes, spares, and open frames
- Applies strike and spare bonuses
- Handles special rules for the 10th frame
- Provides clear API for rolling and scoring

Author: Aashish Sagar Basyal

"""

class BowlingGame:
    """
    BowlingGame class represents a single bowling match.
    
    Attributes:
        rolls (list): Stores the result of each roll in the game.
    """

    def __init__(self):
        """
        Initialize a new bowling game.
        
        Rolls are stored in a list. 
        Each roll represents the number of pins knocked down.
        """
        self.rolls = []

    # -----------------------------------------------------------
    # Game Play Methods
    # -----------------------------------------------------------

    def roll(self, pins: int):
        """
        Record a single roll in the game.

        Args:
            pins (int): Number of pins knocked down in this roll.
        
        Example:
            game.roll(7)  # Knocked down 7 pins in this roll
        """
        self.rolls.append(pins)

    # -----------------------------------------------------------
    # Scoring System
    # -----------------------------------------------------------

    def score(self) -> int:
        """
        Calculate the final score for the bowling game.

        Scoring rules:
        - Strike: 10 + pins from next 2 rolls
        - Spare: 10 + pins from next roll
        - Open Frame: Sum of the two rolls in the frame
        - 10th Frame: May include up to 3 rolls if strike/spare is scored

        Returns:
            int: Total score for the game.
        """
        score = 0
        roll_index = 0

        for frame in range(10):   # Standard 10 frames
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2

        return score

    # -----------------------------------------------------------
    # Helper Methods
    # -----------------------------------------------------------

    def _is_strike(self, roll_index: int) -> bool:
        """
        Check if the roll at roll_index is a strike.

        Args:
            roll_index (int): Position in the rolls list.

        Returns:
            bool: True if strike, else False.
        """
        return self.rolls[roll_index] == 10

    def _is_spare(self, roll_index: int) -> bool:
        """
        Check if the two rolls at roll_index and roll_index+1 form a spare.

        Args:
            roll_index (int): Position of first roll in a frame.

        Returns:
            bool: True if spare, else False.
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _strike_bonus(self, roll_index: int) -> int:
        """
        Get bonus score for a strike (next 2 rolls).

        Args:
            roll_index (int): Index of the strike roll.

        Returns:
            int: Bonus score.
        """
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def _spare_bonus(self, roll_index: int) -> int:
        """
        Get bonus score for a spare (next 1 roll).

        Args:
            roll_index (int): Index of the first roll of the spare.

        Returns:
            int: Bonus score.
        """
        return self.rolls[roll_index + 2]

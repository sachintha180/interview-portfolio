class LapTracker:
    """A record of one runner's lap times, with undo and the fastest lap.

    Attributes:
        laps: The lap times in whole seconds, as a stack, latest last.
    """

    def __init__(self) -> None:
        """Create a tracker with no laps."""
        raise NotImplementedError

    def record(self, seconds: int) -> None:
        """Record a lap time as the latest lap, in O(1) time.

        Args:
            seconds: The lap time in whole seconds.
        """
        raise NotImplementedError

    def undo(self) -> int:
        """Remove the latest lap and return its time, in O(1) time.

        Returns:
            The lap time removed, in seconds.

        Raises:
            IndexError: If no lap is recorded, with the message
                "Nothing to undo."
        """
        raise NotImplementedError

    def fastest_lap(self) -> int:
        """Return the fastest lap time still recorded, in O(1) time.

        Returns:
            The lowest lap time still recorded, in seconds.

        Raises:
            IndexError: If no lap is recorded, with the message
                "No laps recorded."
        """
        raise NotImplementedError

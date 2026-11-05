class SaleNode:
    """One node of a sales log, holding one sale.

    Attributes:
        sale: The sale this node holds.
        previous: The node before this one, or None at the front of the log.
        next: The node after this one, or None at the end of the log.
    """

    def __init__(self, sale: dict[str, str | int]) -> None:
        """Wrap a sale in a new node that links to no other node.

        Args:
            sale: The sale to hold.
        """
        raise NotImplementedError


class SalesLog:
    """A grocery shop's sales, kept in order of time as a doubly linked list.

    The earliest sale is at the front and the latest sale is at the end.
    """

    def __init__(self) -> None:
        """Create an empty log."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of sales in the log, in O(1) time."""
        raise NotImplementedError

    def append(self, sale: dict[str, str | int]) -> None:
        """Add a sale at the end of the log, in O(1) time.

        Args:
            sale: The new sale.
        """
        raise NotImplementedError

    def newest(self, count: int) -> list[dict[str, str | int]]:
        """Return up to count sales, newest first, in O(count) time.

        Args:
            count: The most sales to return.

        Returns:
            A list of up to count sales.

        Raises:
            ValueError: If count is below 0, with the message
                "count must not be negative."
        """
        raise NotImplementedError

    def drop_before(self, timestamp: int) -> int:
        """Remove every sale whose timestamp is below `timestamp`.

        Runs in O(n) time, where n is the number of sales removed. A sale
        at exactly `timestamp` stays.

        Args:
            timestamp: The earliest timestamp to keep.

        Returns:
            The number of sales removed.
        """
        raise NotImplementedError

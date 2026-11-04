class Editor:
    """An editor for one item's price, with undo and redo.

    Attributes:
        price: The item's current price in rupees.
        undo_stack: The prices that undo can put back, latest last.
        redo_stack: The prices that redo can put back, latest last.
    """

    def __init__(self, price: int) -> None:
        """Create an editor for an item, with nothing to undo or redo.

        Args:
            price: The item's first price in rupees.
        """
        raise NotImplementedError

    def edit(self, price: int) -> None:
        """Change the item's price, in O(1) time.

        The change can be undone. Every change waiting to be redone is
        forgotten.

        Args:
            price: The new price in rupees.
        """
        raise NotImplementedError

    def undo(self) -> None:
        """Take back the latest change not yet undone, in O(1) time.

        Raises:
            IndexError: If no change is left to undo, with the message
                "Nothing to undo."
        """
        raise NotImplementedError

    def redo(self) -> None:
        """Put back the latest change that was undone, in O(1) time.

        Raises:
            IndexError: If no change is left to redo, with the message
                "Nothing to redo."
        """
        raise NotImplementedError

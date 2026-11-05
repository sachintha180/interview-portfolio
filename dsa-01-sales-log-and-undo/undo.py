class Editor:
    """An editor for one item's price, with undo and redo.

    Attributes:
        price: The item's current price in rupees.
        undo_stack: The prices undo can put back, with the latest price on top.
        redo_stack: The prices redo can put back, with the latest price on top.
    """

    def __init__(self, price: int) -> None:
        """Create an editor for an item, with nothing to undo or redo.

        Args:
            price: The item's first price in rupees.
        """
        raise NotImplementedError

    def edit(self, price: int) -> None:
        """Change the item's price, in O(1) time.

        Undo can take this change back. The edit clears every change
        waiting to be redone.

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
        """Put back the latest change that undo took back, in O(1) time.

        Raises:
            IndexError: If no change is left to redo, with the message
                "Nothing to redo."
        """
        raise NotImplementedError

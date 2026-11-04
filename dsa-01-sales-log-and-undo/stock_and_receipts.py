def longest_sold_out_streak(
    stock_flags: list[dict[str, str | int | bool]], item_code: str
) -> int:
    """Return the most days in a row on which an item sold out.

    Runs in O(n) time and O(1) extra space, where n is the number of flags.

    Args:
        stock_flags: One flag for each item on each day, in order of day.
        item_code: The item to count.

    Returns:
        The longest run of sold-out days, or 0 if the item never sold out.
    """
    raise NotImplementedError


def receipt_template_balanced(template: str) -> bool:
    """Return whether every bracket in a receipt template closes in order.

    The brackets are { with }, [ with ], and ( with ). Runs in O(n)
    time, where n is the number of characters.

    Args:
        template: The receipt template.

    Returns:
        True if every bracket closes in the right order, and False otherwise.
    """
    raise NotImplementedError

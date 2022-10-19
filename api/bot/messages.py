WELCOME_MESSAGE = (
    "Hi!\nI use the coinmarketcap API.\nTo get the price of a coin, "
    "enter its name or ticker (`Bitcoin` | `BTC`, `Dogecoin` | `Doge`)\n"
    "To get more information about a coin, enter `info` or `i`."
)


def display_error_message(type_error: str) -> str:
    """
    Takes an error type and returns an appropriate message
    """
    return {
        "session": "Session error! Enter coin (e.g. bitcoin, doge)",
        "match": "Match error!",
        "unknown": "Sorry! Unknown error!",
    }[type_error]

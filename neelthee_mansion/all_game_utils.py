from .utils import *
from re import *


def ask_for_consent(text: str) -> bool:
    while True:
        type_text(f"{text}? Y/N")
        anser = str(input(">")).lower().strip()
        if anser == "y":
            return True
        elif anser == "n":
            return False
        else:
            type_text("That wasn't Y or N")

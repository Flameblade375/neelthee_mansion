from .utils import *
from re import *


def ask_for_consent(text: str, text_area) -> bool:
    while True:
        anser = loop_til_valid_input(f"{text}? Y/N", "That wasn't Y or N", Y_N).value
        if anser == "y":
            return True
        else:
            return False

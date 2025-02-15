from .utils import *
from re import *


def ask_for_consent(text: str, text_area) -> bool:
    while True:
        add_text_to_textbox(text_area, f"{text}? Y/N")
        anser = loop_til_valid_input("", "That wasn't Y or N", Y_N).Value
        if anser == "y":
            return True
        elif anser == "n":
            return False

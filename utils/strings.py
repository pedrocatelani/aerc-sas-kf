import unicodedata
import re


def remove_accents(entry_string: str) -> str:
    final_string = "".join(
        char
        for char in unicodedata.normalize("NFD", entry_string)
        if unicodedata.category(char) != "Mn"
    )

    final_string = re.sub(r"[^A-Za-z0-9 ]+", "", final_string)
    return final_string

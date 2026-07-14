from unittest import TestCase
from collections.abc import Callable


run_cases: list[TestCase] = [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".doc",
        "document",
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".png",
        "image",
    ),
]

for file in run_cases:
    for i in file:
        print(i)

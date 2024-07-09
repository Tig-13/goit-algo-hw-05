import re
from typing import Callable

def generator_numbers(text: str):
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    for match in pattern.finditer(text):
        yield float(match.group())

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))
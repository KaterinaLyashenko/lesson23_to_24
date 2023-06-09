import re
from typing import Iterable, Generator, List, Any, Set


def filter_query(value: str, data: Iterable[str]) -> filter:
    return filter(lambda x: value in x, data)

def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)

def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit: int = int(value)
    return list(data)[:limit]

def map_query(value: str, data: Generator) -> map:
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)

def regex_query(value: str, data: Iterable[str]) -> Iterable[str]:
    pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)

#!/usr/bin/env python3
"""
a function that does the pagination
of an api
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    pagination function
    that returns a turple
    shows the starting index
    and the ending index
    """
    startIndex = (page - 1) * page_size
    endingIndex = (startIndex + page_size)
    return (startIndex, endingIndex)

#!/usr/bin/env python3
"""
a function that does the pagination
of an api
"""


import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        this is a function that finds pages depending
        on the size of the page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]

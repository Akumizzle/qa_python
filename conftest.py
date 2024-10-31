from main import BooksCollector

import pytest
from test_data import test_books

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def fill_collector(collector):
    collector.add_new_book(list(test_books.keys())[0])
    collector.set_book_genre((list(test_books.keys())[0]), test_books[(list(test_books.keys())[0])]) #не знаю пока можно ли вызвать навание и жанр из файла из словаря более лаконичным способом
    return collector





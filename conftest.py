from main import BooksCollector

import pytest

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    collector.add_new_book('Ведьмак')
    collector.set_book_genre('Ведьмак', 'Фантастика')

    return collector


@pytest.fixture(scope='function')
def collector_favorite():
    collector = BooksCollector()
    collector.add_new_book('Ведьмак')
    collector.set_book_genre('Ведьмак', 'Фантастика')
    collector.add_book_in_favorites('Ведьмак')

    return collector





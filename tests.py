from gc import collect

from main import BooksCollector
import pytest
from test_data import test_books


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
    #    # создаем экземпляр (объект) класса BooksCollector
    #    collector = BooksCollector()

    #    # добавляем две книги
    #    collector.add_new_book('Гордость и предубеждение и зомби')
    #    collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    #    # проверяем, что добавилось именно две
    #    # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #    assert len(collector.get_books_rating()) == 2
    ## напиши свои тесты ниже
    ## чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_two_books(self,collector):                       # пример теста был неправильно написан
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre())==2
    @pytest.mark.parametrize('name,genre', [['Ведьмак', 'Фантастика'], ['фыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы', 'Детективы'],['в', 'Комедии']])
    def test_set_book_genre_set_genre_to_book(self,name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name]==genre


    def test_set_book_genre_genre_not_in_list_flase(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фэнтези')
        assert collector.books_genre['Ведьмак'] == ''

    def test_get_book_genre_book_in_list_true(self,collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        assert collector.get_book_genre('Ведьмак')=='Фантастика'

    def test_get_book_genre_book_not_in_list_false(self,collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        assert collector.get_book_genre('Война и мир')==None

    def test_get_books_with_specific_genre_genre_in_list_true(self,collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика')==['Ведьмак']

    def test_get_books_genre_get_added_books(self,fill_collector):
        assert fill_collector.get_books_genre()=={'Ведьмак':'Фантастика'}

    def test_get_books_genre_get_empty_list(self,collector):
        empty_list=collector.get_books_genre()
        assert len(empty_list)==0

    def test_get_books_for_children_get_books_with_correct_genre(self,fill_collector):
        fill_collector.add_new_book('Сияние')
        fill_collector.set_book_genre('Сияние', 'Ужасы')
        assert fill_collector.get_books_for_children()==['Ведьмак']

    def test_add_book_in_favorites_add_new_book(self,fill_collector):
        fill_collector.add_book_in_favorites((list(test_books.keys())[0])) #не знаю пока можно ли вызвать навание более лаконичным способом
        assert fill_collector.favorites==[(list(test_books.keys())[0])]


    def test_delete_book_from_favorites_delete_from_list_true(self,fill_collector):
        fill_collector.add_book_in_favorites('Ведьмак')
        fill_collector.delete_book_from_favorites('Ведьмак')
        assert len(fill_collector.favorites) == 0


    def test_get_list_of_favorites_books_get_list(self,fill_collector):
        fill_collector.add_book_in_favorites('Ведьмак')
        fill_collector.add_new_book('Война и мир')
        fill_collector.add_book_in_favorites('Война и мир')
        assert len(fill_collector.get_list_of_favorites_books())==2






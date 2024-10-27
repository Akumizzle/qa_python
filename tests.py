from gc import collect

from main import BooksCollector
import pytest


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

    def test_add_new_book_add_two_books(self):                       # пример теста был неправильно написан
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre())==2

    @pytest.mark.parametrize('name,genre', [['Ведьмак', 'Фантастика'], ['Десять негритят', 'Детективы']])
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

        assert collector.get_book_genre('Ведьмак')=='Фантастика'

    def test_get_book_genre_book_not_in_list_false(self,collector):

        assert collector.get_book_genre('Война и мир')==None

    def test_get_books_with_specific_genre_genre_in_list_true(self,collector):

        assert collector.get_books_with_specific_genre('Фантастика')==['Ведьмак']

    def test_get_books_genre_get_added_books(self,collector):

        assert collector.get_books_genre()=={'Ведьмак':'Фантастика'}

    def test_get_books_genre_get_empty_list(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_books_for_children_get_books_with_correct_genre(self,collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_for_children()==['Ведьмак']

    def test_add_book_in_favorites_add_new_book(self,collector):
        collector.add_book_in_favorites('Ведьмак')

        assert collector.favorites==['Ведьмак']


    @pytest.mark.parametrize('name', ['Ведьмак','Война и мир'])
    def test_delete_book_from_favorites_delete_from_list_true(self,name):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == 1


    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert len(collector.get_list_of_favorites_books())==2





